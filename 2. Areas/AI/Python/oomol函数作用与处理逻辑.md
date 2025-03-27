 ## 提取主要文本内容
 
 [GitHub - oomol-lab/pdf-craft: convert PDF files into various other formats. ](https://github.com/oomol-lab/pdf-craft)
 `analyse_main_texts` 的作用和逻辑。

**总体目标:**

这个函数的核心目标是处理从一系列页面（很可能来自 PDF 等文档）中提取的主要文本内容。它执行以下操作：

1.  **分块处理：** 根据大语言模型 (LLM) 的 Token 限制，将这些页面分成合适的块（Chunk）。
2.  **上下文构建：** 为每个块准备输入数据，包括页面内容、相关的引用文献信息，以及上一个块生成的摘要（以保持上下文连贯）。
3.  **LLM 分析：** 将每个块的数据发送给 LLM 进行分析和结构化处理。
4.  **结果处理：** 解析 LLM 返回的结果，提取新生成的摘要和结构化的内容，并正确处理引用文献信息。
5.  **输出写入：** 将每个块处理后的结构化结果写入到一个文件 (`ChunkFile`) 中。
6.  **辅助功能：** 包含进度报告、过滤索引页和基于“间隔页”（gap pages）生成的内容等机制。

**分步详解:**

1.  **初始化与 Token 计算:**
    *   计算基础提示（Prompt）所需的 Token 数量 (`prompt_tokens`)。
    *   通过从总请求 Token 限制 (`request_max_tokens`) 中减去提示 Token 数，计算出实际可用于页面数据的最大 Token 数 (`data_max_tokens`)。
    *   如果 `request_max_tokens` 不足以容纳提示本身，则抛出错误。
    *   初始化一个 `_CitationLoader` 对象，用于根据页面索引加载引用文献数据。

2.  **页面分组/分块:**
    *   使用 `_extract_page_text_infos` 从 `pages` 列表中提取所需信息。
    *   调用 `split` 函数，根据 `max_segment_count`（由 `data_max_tokens` 决定）以及 `gap_rate` 和 `tail_rate` 参数，将页面信息 (`resources`) 分成多个 `groups`。每个 `group` 代表一个适合单次 LLM 请求处理的页面块。
    *   如果提供了报告回调，则报告创建的分组数量。

3.  **遍历处理每个分组:**
    *   初始化 `summary` 为 `None`。这个变量将存储上一个块 LLM 生成的摘要，并作为上下文传递给当前块。
    *   循环遍历每个 `group`，获取原始的起始/结束页面索引 (`start_idx`, `end_idx`) 以及该组的任务数据 (`task_group`)。

4.  **为每个分组准备 LLM 输入:**
    *   `get_and_clip_pages`: 获取当前 `group` 对应的 `PageInfo` 对象列表，可能进行裁剪（具体取决于函数实现）。
    *   **索引页过滤:** 如果提供了 `index` 对象，则过滤掉被识别为索引页的页面。如果一个分组过滤后不包含任何非索引页，则跳过该分组。
    *   **构建输入 XML (`raw_pages_root`):**
        *   创建一个根 XML 元素 `<pages>`。
        *   遍历当前分组的页面列表 (`page_xml_list`)。
        *   获取页面的 XML 表示 (`page_xml.xml`)。
        *   在该页面元素上设置 `idx` 属性（表示它在**当前这个分组/块内**的 1-based 索引）。
        *   使用 `_CitationLoader` 加载该页面**原始索引**对应的引用文献。如果存在，则附加到页面的 XML 元素中。
        *   将处理后的页面元素附加到 `raw_pages_root`。
    *   **添加上文摘要:** 如果 `summary`（来自上一次迭代）不为 `None`，则创建一个 `<summary>` 元素，设置其文本内容，并附加到 `raw_pages_root`。这为跨块处理提供了上下文连续性。

5.  **与 LLM 交互:**
    *   初始化 `AssetMatcher`（可能用于处理图片、表格等资源，细节未完全展示）并注册输入 XML。
    *   调用 `llm.request_xml`，将构建好的 `raw_pages_root` XML 和任务类型 "main_text" 发送给 LLM。
    *   接收 LLM 返回的 XML 响应 (`response_xml`)。

6.  **处理 LLM 输出:**
    *   **设置分块 XML:** 创建用于输出的根元素 `<chunk>`，并添加表示**原始**文档页面范围的 `start-idx` 和 `end-idx` 属性（1-based）。
    *   更新 `AssetMatcher`。
    *   **提取摘要:** 在响应中找到 `<abstract>` 元素，断言其存在，并将其直接附加到 `chunk_xml`。同时，用这个摘要的文本内容更新 `summary` 变量，供**下一次**迭代使用。
    *   **处理内容元素:**
        *   在 `chunk_xml` 内创建一个空的 `<content>` 元素。
        *   遍历 `response_xml` 中 `<content>` 元素下的子元素。
        *   解析 LLM 输出元素上的 `idx` 属性（这个 `idx` 指的是在**输入 `raw_pages_root` 内部**的 1-based 索引）。
        *   **间隔页过滤:** 检查这些索引对应的原始页面中，是否**至少有一个**不是 `is_gap` 页面。这是关键一步，用于避免包含 LLM 可能仅基于填充/间隔页生成的内容。
        *   **重新索引:** 如果内容元素通过了间隔页过滤：
            *   将这些**分组内**的索引 (`k`) 转换回**原始文档的页面索引** (`page_xml_list[k].page_index + 1`)。
            *   将内容子元素 (`child`) 的 `idx` 属性设置为这些**原始页面索引**的逗号分隔字符串。
            *   将处理后的 `child` 元素附加到正在构建的输出 `content_xml` 中。
    *   **最终引用处理:** 调用 `_collect_citations_and_reallocate_ids`。此函数可能比较原始发送的引用和最终包含在 `chunk_xml` 中的内容相关的引用，收集真正需要的引用，可能会重新分配它们的 ID，并返回一个新的 `<citations>` XML 元素（如果存在相关引用）。然后将其附加到 `chunk_xml`。

7.  **写入输出与报告:**
    *   `file.atomic_write_chunk`: 将完整的 `chunk_xml`（包含摘要、过滤/重新索引后的内容、相关引用）写入到输出文件系统，并关联原始的页面范围 (`start_idx`, `end_idx`)。“原子写入”意味着它确保写入操作要么完全成功，要么完全不执行，防止部分写入导致文件损坏。
    *   如果设置了 `report_progress` 回调，则调用它，表示已处理完一个块。

**关键特性与逻辑:**

*   **分块处理 (Chunking):** 通过将大文档分解为适合 LLM 处理的大小来处理大型文档。
*   **上下文传播 (Context Propagation):** 通过在输入 XML 中传递 `<summary>` 标签，将上一个块的摘要信息传递给下一个块。
*   **健壮的索引管理 (Robust Indexing):** 仔细管理不同的索引范围：原始文档页面索引、分组内部用于 LLM 输入的索引，以及最终输出时映射回原始索引。
*   **XML 数据格式 (XML Data Format):** 使用 XML 来结构化 LLM 的输入和存储结构化的输出。
*   **引用文献管理 (Citation Management):** 按页加载引用，发送给 LLM，然后根据 LLM 的最终输出筛选和重新分配相关引用。
*   **内容过滤 (Filtering):** 明确过滤掉指定的索引页以及可能仅由间隔页生成的内容。
*   **错误处理 (Error Handling):** 对 `request_max_tokens` 进行了基本检查。
*   **报告机制 (Reporting):** 提供可选的回调函数用于报告处理步骤和进度。
*   **资源处理 (Asset Handling - 暗示):** 使用了 `AssetMatcher`，表明可能存在处理非文本元素（如图像、表格）的机制（虽然细节未在此代码段中完全展示）。