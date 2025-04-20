好的，我来解释一下 `AgentCapabilities` 类中的 `streaming`、`pushNotifications` 和 `stateTransitionHistory` 这几种能力。

**AgentCapabilities 类**

`AgentCapabilities` 类用于描述 Agent 具备的能力。

```python
class AgentCapabilities(BaseModel):
    streaming: bool = False
    pushNotifications: bool = False
    stateTransitionHistory: bool = False
```

*   **`streaming: bool = False`**:  表示 Agent 是否支持流式传输。
    *   **流式传输 (streaming)**：流式传输是指将数据分成小块，并逐块地传输给客户端。客户端可以在接收到部分数据后就开始处理，而不需要等待所有数据都传输完毕。
    *   **适用场景**：流式传输适用于需要实时传输大量数据的场景，例如音视频直播、实时数据分析等。
    *   **`streaming=False`**:  表示 Agent 不支持流式传输。
*   **`pushNotifications: bool = False`**:  表示 Agent 是否支持推送通知。
    *   **推送通知 (push notifications)**：推送通知是指服务器主动向客户端发送通知消息，而不需要客户端主动请求。
    *   **适用场景**：推送通知适用于需要实时通知客户端的场景，例如消息提醒、事件通知等。
    *   **`pushNotifications=False`**:  表示 Agent 不支持推送通知。
*   **`stateTransitionHistory: bool = False`**:  表示 Agent 是否支持状态转换历史记录。
    *   **状态转换历史记录 (state transition history)**：状态转换历史记录是指记录 Agent 状态变化的过程。
    *   **适用场景**：状态转换历史记录适用于需要跟踪 Agent 状态变化的场景，例如调试、监控等。
    *   **`stateTransitionHistory=False`**:  表示 Agent 不支持状态转换历史记录。
