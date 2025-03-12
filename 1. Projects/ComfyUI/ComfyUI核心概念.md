当然！ComfyUI 是一个基于节点的工作流程系统，用于 Stable Diffusion 和其他生成式 AI 模型。理解 ComfyUI 的术语对于有效地使用它至关重要。以下是 ComfyUI 中最常用的 100 个术语的注释，旨在帮助您更好地理解和使用 ComfyUI：

**核心概念 (Core Concepts):**

1. **工作流程 (Workflow):** ComfyUI 的核心，由一系列相互连接的节点组成，定义了图像生成的整个流程。
2. **节点 (Node):** 工作流程的基本构建块，每个节点执行特定的任务，例如加载模型、采样、VAE 解码、图像处理等。
3. **连线 (Connection/Wire):** 节点之间用于传递数据（例如图像、模型、潜在空间等）的连接线。
4. **输入 (Input):** 节点左侧的圆形接口，用于接收来自其他节点的数据或用户参数。
5. **输出 (Output):** 节点右侧的圆形接口，用于将节点处理后的数据传递给其他节点。
6. **参数 (Parameter):** 节点内部可以调整的设置项，用于控制节点的行为，例如采样步数、CFG 尺度、种子等。
7. **预览 (Preview):** ComfyUI 界面中显示节点输出结果的区域，通常用于图像节点，可以实时查看图像生成或处理的中间结果。
8. **队列提示词 (Queue Prompt):** 启动工作流程执行的按钮，点击后 ComfyUI 会按照节点连接顺序执行工作流程。
9. **执行顺序 (Execution Order):** ComfyUI 按照节点之间的连线和依赖关系自动确定节点的执行顺序。
10. **保存工作流程 (Save Workflow):** 将当前工作流程保存为 JSON 文件 (`.json` 或 `.ckpt` 扩展名)，以便稍后加载和复用。
11. **加载工作流程 (Load Workflow):** 从 JSON 文件中加载已保存的工作流程。
12. **组 (Group):** 将多个节点组合在一起，方便组织和移动工作流程。
13. **注释 (Annotation/Comment):** 添加到节点或工作流程上的文本说明，用于解释节点的功能或工作流程的步骤。
14. **干净工作区 (Clear Workspace):** 清空当前工作流程画布上的所有节点和连线。
15. **节点菜单 (Node Menu):** 右键单击画布空白处弹出的菜单，用于添加新的节点。
16. **上下文菜单 (Context Menu):** 右键单击节点或连线弹出的菜单，提供节点或连线的特定操作选项。
17. **快捷键 (Hotkeys):** ComfyUI 的快捷键，用于快速执行常用操作，例如添加节点、移动画布、删除节点等。
18. **自定义节点 (Custom Node):** 用户可以通过 Python 脚本创建的节点，扩展 ComfyUI 的功能。
19. **管理器 (Manager):** ComfyUI 的管理器界面，用于安装、更新和管理自定义节点、模型和其他资源。
20. **捆绑包 (Bundle):** 一组相关的自定义节点和资源的集合，方便用户安装和使用特定功能的扩展。

**模型和资源 (Models & Resources):**

1. **模型 (Model):** 通常指 Stable Diffusion 模型，用于生成图像的核心组件，包含 Checkpoint 模型、VAE 模型、CLIP 模型等。
2. **Checkpoint 模型 (.ckpt/.safetensors):** Stable Diffusion 的主要模型文件，包含了生成图像所需的所有权重信息，例如 Stable Diffusion v1.5, SDXL 等。
3. **VAE 模型 (.vae.pt/.safetensors):** 变分自编码器模型，用于将潜在空间表示与像素空间图像相互转换，影响图像的解码质量和色彩。
4. **CLIP 模型 (CLIP Model):** 对比语言-图像预训练模型，用于理解和处理文本提示词，引导图像生成。
5. **Lora 模型 (.safetensors):** 低秩适应模型，用于在不改变 Checkpoint 模型主体的情况下，微调模型的风格或特定对象的生成效果，文件体积小。
6. **ControlNet 模型 (.safetensors):** 控制网络模型，用于通过额外的控制条件（例如草图、深度图、姿势等）来引导图像生成，实现更精确的控制。
7. **T2I Adapter 模型 (.safetensors):** 文本到图像适配器模型，类似于 ControlNet，但结构和控制方式略有不同，也用于条件控制图像生成。
8. **IP-Adapter 模型 (.safetensors):** 图像提示适配器模型，用于使用参考图像来引导生成图像的风格或构图。
9. **Embedding (Textual Inversion) (.pt/.safetensors):** 文本反演，通过学习少量图像来创建一个新的文本 embedding，用于生成特定风格或对象的图像，通常用于风格迁移或角色一致性。
10. **Hypernetwork (.pt/.safetensors):** 超网络，一种辅助模型，用于在生成过程中动态调整 Checkpoint 模型的权重，实现风格变化或细节增强。
11. **预处理器 (Preprocessor):** ControlNet 或 T2I Adapter 模型的前处理步骤，用于将输入图像转换为模型可以识别的控制信号，例如边缘检测、姿势提取等。
12. **模型路径 (Model Path):** ComfyUI 中配置模型文件存放位置的设置。
13. **模型管理器 (Model Manager):** 用于方便管理和下载各种模型的工具或节点。
14. **模型加载节点 (Load Model Node):** 用于加载 Checkpoint、VAE、CLIP 等模型的 ComfyUI 节点。
15. **模型采样器 (Model Sampler):** 在潜在空间中进行采样的算法，例如 Euler, LMS, DDIM, DPM++ 等。

**图像生成流程 (Image Generation Process):**

1. **提示词 (Prompt):** 用于描述期望生成图像的文本描述，包括正面提示词 (Positive Prompt) 和负面提示词 (Negative Prompt)。
2. **正面提示词 (Positive Prompt):** 描述希望图像包含的元素和风格。
3. **负面提示词 (Negative Prompt):** 描述不希望图像包含的元素或需要避免的风格，用于优化图像质量。
4. **种子 (Seed):** 随机数种子，用于控制生成图像的随机性，相同的种子和提示词会生成相似的图像。
5. **采样步数 (Steps/Sampling Steps):** 采样器在潜在空间中迭代去噪的次数，步数越多，生成图像的细节通常更丰富，但计算时间也更长。
6. **CFG 尺度 (CFG Scale/Guidance Scale):** Classifier-Free Guidance Scale，控制提示词对图像生成的影响程度，数值越高，提示词引导性越强，但可能导致图像质量下降或过度饱和。
7. **采样器 (Sampler):** 用于在潜在空间中进行采样的算法，不同的采样器算法有不同的特性和生成效果。
8. **去噪器 (Denoiser):** 采样过程中的核心组件，负责根据模型和提示词对潜在空间噪声进行迭代去噪。
9. **潜在空间 (Latent Space):** 模型内部表示图像信息的低维度空间，采样和去噪过程都在潜在空间中进行。
10. **潜在变量 (Latent Variable):** 潜在空间中的数据表示，通常是一个多维数组，包含了图像的压缩信息。
11. **编码器 (Encoder):** VAE 模型的一部分，将像素空间图像编码压缩到潜在空间。
12. **解码器 (Decoder):** VAE 模型的一部分，将潜在空间表示解码还原为像素空间图像。
13. **分辨率 (Resolution/Image Size):** 生成图像的宽度和高度，通常以像素为单位。
14. **批次大小 (Batch Size):** 一次性生成图像的数量，批次越大，GPU 显存占用越高。
15. **图像格式 (Image Format):** 生成图像的文件格式，例如 PNG, JPEG, WEBP 等。
16. **图像保存节点 (Save Image Node):** 用于将生成的图像保存到本地硬盘的 ComfyUI 节点。
17. **图像加载节点 (Load Image Node):** 用于从本地硬盘加载图像到 ComfyUI 工作流程的节点。
18. **图像编辑节点 (Image Edit Node):** 用于对图像进行编辑和处理的节点，例如调整大小、裁剪、旋转、滤镜等。
19. **图生图 (Img2Img):** 基于输入图像进行图像生成的模式，用于图像风格迁移、图像修复、局部重绘等。
20. **文生图 (Txt2Img):** 基于文本提示词进行图像生成的模式。
21. **重绘 (Inpainting):** 图像局部重绘，通过遮罩 (Mask) 指定需要重绘的区域，并使用提示词引导模型在指定区域生成新的内容。
22. **放大 (Upscale):** 提高图像分辨率的操作，通常使用放大模型 (Upscaler Model) 或算法来实现，例如 Lanczos, ESRGAN, RealESRGAN 等。
23. **放大模型 (Upscaler Model):** 用于图像放大的模型，可以提高图像分辨率并尽可能保持图像细节和质量。
24. **平铺 (Tiling/Seamless Tiling):** 使图像能够无缝平铺的技术，常用于生成纹理、背景等可以重复平铺的图像。
25. **循环 (Loop):** 工作流程中的循环结构，可以重复执行某些节点或子流程，例如批量生成图像、迭代优化参数等。
26. **条件控制 (Conditioning):** ControlNet, T2I Adapter 等模型使用的控制信号，用于引导图像生成。
27. **提示词编码 (Prompt Encoding):** 将文本提示词转换为模型可以理解的向量表示的过程，CLIP 模型负责提示词编码。

**常用节点类型 (Common Node Types):**

1. **Checkpoints:** 用于加载 Checkpoint 模型的节点。
2. **Load Image:** 用于加载本地图像文件的节点。
3. **Save Image:** 用于保存生成图像的节点。
4. **CLIP Text Encode:** 用于将文本提示词编码为 CLIP 向量的节点。
5. **VAE Decode:** 用于将潜在空间表示解码为像素空间图像的节点。
6. **VAE Encode:** 用于将像素空间图像编码为潜在空间表示的节点。
7. **KSampler:** 核心采样节点，用于在潜在空间中进行采样和去噪，是图像生成的关键步骤。
8. **Conditioning (Positive & Negative):** 用于输入正面和负面提示词条件的节点，通常与 CLIP Text Encode 节点配合使用。
9. **ControlNet Loader:** 用于加载 ControlNet 模型的节点。
10. **ControlNet Apply:** 用于应用 ControlNet 控制的节点，通常与 KSampler 节点配合使用。
11. **T2I Adapter Loader:** 用于加载 T2I Adapter 模型的节点。
12. **T2I Adapter Apply:** 用于应用 T2I Adapter 控制的节点。
13. **IP-Adapter Loader:** 用于加载 IP-Adapter 模型的节点。
14. **IP-Adapter Apply:** 用于应用 IP-Adapter 控制的节点。
15. **Lora Loader:** 用于加载 Lora 模型的节点。
16. **Hypernetwork Loader:** 用于加载 Hypernetwork 模型的节点。
17. **Upscale Image:** 用于放大图像的节点，可以使用不同的放大算法或模型。
18. **Mask Editor:** 用于创建和编辑图像遮罩的节点，常用于重绘 (Inpainting) 功能。
19. **Preview Image:** 用于在 ComfyUI 界面中预览图像的节点。
20. **Reroute:** 用于整理和简化复杂工作流程的节点，可以像导线一样连接不同的节点。
21. **Primitive Node (Primitive):** 用于输入基本数据类型（例如数字、文本、布尔值）的节点。
22. **Multiply:** 用于数值乘法运算的节点。
23. **Divide:** 用于数值除法运算的节点。
24. **Add:** 用于数值加法运算的节点。
25. **Subtract:** 用于数值减法运算的节点。
26. **String Interpolate:** 用于字符串插值和格式化的节点，可以将变量值嵌入到文本字符串中。
27. **Switch:** 条件开关节点，根据条件选择不同的数据流路径。
28. **Latent Scale By Factor:** 用于缩放潜在空间表示的节点。

**用户界面和操作 (User Interface & Operations):**

1. **画布 (Canvas):** ComfyUI 的主要界面，用于创建和编辑工作流程。
2. **侧边栏 (Sidebar):** ComfyUI 界面左侧的工具栏，包含常用操作按钮和节点列表。
3. **节点属性面板 (Node Properties Panel):** 选中节点后在界面右侧显示的面板，用于调整节点的参数设置。
4. **状态栏 (Status Bar):** ComfyUI 界面底部的状态栏，显示当前工作流程的执行状态、进度和提示信息。
5. **拖拽 (Drag and Drop):** ComfyUI 中常用的操作方式，例如拖拽节点、连线、图像等。
6. **缩放 (Zoom):** 放大或缩小 ComfyUI 画布的视图。
7. **平移 (Pan):** 移动 ComfyUI 画布的视图。
8. **框选 (Box Selection):** 使用鼠标框选多个节点，进行批量操作，例如移动、删除、分组等。
9. **节点对齐 (Node Alignment):** ComfyUI 提供的自动对齐节点的功能，使工作流程更整洁。
10. **工作流程分享 (Workflow Sharing):** 将 ComfyUI 工作流程导出为图片或 JSON 文件，方便与其他用户分享。

希望这份 ComfyUI 术语注释能够帮助您更好地理解和使用 ComfyUI！ComfyUI 的强大之处在于其灵活性和可扩展性，掌握这些术语将是您深入探索 ComfyUI 世界的第一步。 祝您使用愉快！