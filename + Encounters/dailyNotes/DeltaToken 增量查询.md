---
aliases: 
theme: 
priority: false
---

`DeltaToken` 是 Microsoft Graph API 中用于增量查询（delta query）的一个概念。它是一个特殊的令牌，用来跟踪和获取自上次请求以来发生更改的数据。当你使用增量查询时，`DeltaToken` 使得应用程序能够高效地同步数据，而无需每次都检索全部数据集。

### DeltaToken 的工作原理

1. **初始请求**：你发起一个增量查询的初始请求，这将返回自某个时间点以来的所有更改。响应中会包含一个 `@odata.deltaLink` 或 `@odata.nextLink`，其中包含了 `deltatoken`。

2. **后续请求**：在后续的增量查询请求中，你需要使用上一次响应中的 `deltatoken` 来继续获取新的更改。这个 `deltatoken` 会被附加到请求 URL 中，以便服务器知道从哪里开始提供最新的更改。

3. **结束条件**：当没有更多的更改可以返回时，服务端会在响应中返回一个空的结果集，并且不再提供新的 `deltatoken`。这时，你可以停止增量查询，直到下一次需要同步数据时再重新开始。

### 使用 DeltaToken 的好处

- **减少网络流量**：只传输发生了更改的数据，而不是整个数据集。
- **提高效率**：减少了处理大量数据的时间，特别是在大数据集的情况下。
- **节省成本**：对于按请求次数计费的服务，减少了不必要的请求。

### 示例

假设你在追踪用户的邮件变化，以下是可能的流程：

1. **第一次增量查询**：

   ```http
   GET https://graph.microsoft.com/v1.0/me/mailFolders/inbox/messages/delta
   ```

   响应中可能会包含一些新邮件或更新过的邮件信息，并且会有一个 `@odata.deltaLink` 类似如下：

   ```json
   {
     "@odata.context": "https://graph.microsoft.com/v1.0/$metadata#Collection(microsoft.graph.message)",
     "value": [ /* 新邮件或更新过的邮件 */ ],
     "@odata.deltaLink": "https://graph.microsoft.com/v1.0/me/mailFolders/inbox/messages/delta?$deltatoken=opaque_token"
   }
   ```

2. **后续的增量查询**：

   ```http
   GET https://graph.microsoft.com/v1.0/me/mailFolders/inbox/messages/delta?$deltatoken=opaque_token
   ```

   这里 `opaque_token` 就是上一次响应中的 `deltatoken`。这次请求只会返回自上次请求以来的新邮件或更新过的邮件。

通过这种方式，你可以持续跟踪并同步用户邮箱中的更改，而不需要每次下载所有邮件。这对于保持客户端与服务器数据同步非常有用，尤其是在移动应用或实时性要求较高的场景中。
