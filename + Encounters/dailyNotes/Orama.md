---
aliases: 
<<<<<<< HEAD
theme: 
priority: false
=======
categories: 
high_priority: false
>>>>>>> 93a933e (refactor(dailyNotes): update metadata structure for daily notes)
tags:
---
这段TypeScript代码定义了一个名为`OramaManager`的类，用于管理一个基于`Orama`的搜索引擎实例。`Orama`是一个用于构建和查询向量空间索引的库，特别适用于处理大量文本数据。这个类还集成了数据持久化功能，可以将索引保存到数据库中，并在需要时恢复。

### 实现原理

1. **初始化**：在构造函数中接收一个`accountId`，用于标识用户或账户。在`initialize`方法中，根据账户ID从数据库中查找对应的索引数据。如果存在，则恢复索引；否则，创建一个新的索引并保存到数据库中。

2. **插入文档**：`insert`方法用于向索引中插入新的文档。插入后，会调用`saveIndex`方法将索引保存到数据库中。

3. **搜索**：`vectorSearch`方法使用向量搜索来查找与给定提示词最相似的文档。`search`方法则使用文本搜索来查找包含特定关键词的文档。

4. **保存索引**：`saveIndex`方法将当前的索引数据序列化为JSON格式，并保存到数据库中。

### 用途

这个类可以用于构建一个基于文本和向量的搜索引擎，适用于需要处理大量文本数据的应用场景，如邮件搜索、文档检索等。通过使用向量搜索，可以更准确地找到与查询相关的文档。

### 注意事项

1. **依赖库**：代码依赖于`@orama/orama`和`@orama/plugin-data-persistence`库，需要确保这些库已正确安装。

2. **数据持久化**：通过将索引数据保存到数据库中，可以在应用程序重启后恢复索引，避免数据丢失。

3. **性能考虑**：向量搜索的计算量较大，需要考虑性能优化，如使用更高效的向量存储和检索算法。

4. **错误处理**：代码中包含基本的错误处理，如账户未找到时抛出错误。在实际应用中，可能需要更详细的错误处理逻辑。

5. **类型安全**：代码使用了TypeScript，提供了类型检查，有助于减少运行时错误。确保在使用时遵循类型定义。

```js
import { create, insert, search, save, load, type AnyOrama } from "@orama/orama";

import { persist, restore } from "@orama/plugin-data-persistence";

import { db } from "@/server/db";

import { getEmbeddings } from "@/lib/embeddings";

  

export class OramaManager {

    // @ts-ignore

    private orama: AnyOrama;

    private accountId: string;

  

    constructor(accountId: string) {

        this.accountId = accountId;

    }

  

    async initialize() {

        const account = await db.account.findUnique({

            where: { id: this.accountId },

            select: { binaryIndex: true }

        });

  

        if (!account) throw new Error('Account not found');

  

        if (account.binaryIndex) {

            this.orama = await restore('json', account.binaryIndex as any);

        } else {

            this.orama = await create({

                schema: {

                    title: "string",

                    body: "string",

                    rawBody: "string",

                    from: 'string',

                    to: 'string[]',

                    sentAt: 'string',

                    embeddings: 'vector[1536]',

                    threadId: 'string'

                },

            });

            await this.saveIndex();

        }

    }

  

    async insert(document: any) {

        await insert(this.orama, document);

        await this.saveIndex();

    }

  

    async vectorSearch({ prompt, numResults = 10 }: { prompt: string, numResults?: number }) {

        const embeddings = await getEmbeddings(prompt)

        const results = await search(this.orama, {

            mode: 'hybrid',

            term: prompt,

            vector: {

                value: embeddings,

                property: 'embeddings'

            },

            similarity: 0.80,

            limit: numResults,

            // hybridWeights: {

            //     text: 0.8,

            //     vector: 0.2,

            // }

        })

        // console.log(results.hits.map(hit => hit.document))

        return results

    }

    async search({ term }: { term: string }) {

        return await search(this.orama, {

            term: term,

        });

    }

  

    async saveIndex() {

        const index = await persist(this.orama, 'json');

        await db.account.update({

            where: { id: this.accountId },

            data: { binaryIndex: index as Buffer }

        });

    }

}

  

// Usage example:

async function main() {

    const oramaManager = new OramaManager('67358');

    await oramaManager.initialize();

  

    // Insert a document

    // const emails = await db.email.findMany({

    //     where: {

    //         thread: { accountId: '67358' }

    //     },

    //     select: {

    //         subject: true,

    //         bodySnippet: true,

    //         from: { select: { address: true, name: true } },

    //         to: { select: { address: true, name: true } },

    //         sentAt: true,

    //     },

    //     take: 100

    // })

    // await Promise.all(emails.map(async email => {

    //     // const bodyEmbedding = await getEmbeddings(email.bodySnippet || '');

    //     // console.log(bodyEmbedding)

    //     await oramaManager.insert({

    //         title: email.subject,

    //         body: email.bodySnippet,

    //         from: `${email.from.name} <${email.from.address}>`,

    //         to: email.to.map(t => `${t.name} <${t.address}>`),

    //         sentAt: email.sentAt.getTime(),

    //         // bodyEmbedding: bodyEmbedding,

    //     })

    // }))

  
  

    // Search

    const searchResults = await oramaManager.search({

        term: "cascading",

    });

  

    console.log(searchResults.hits.map((hit) => hit.document));

}

  

// main().catch(console.error);
```