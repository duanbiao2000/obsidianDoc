在Yazi项目中，`tracing`库被用作依赖项，可以在`Cargo.toml`文件中找到。这个库是一个用于跟踪和日志记录的库，它提供了一套完整的跟踪和日志记录功能，包括跟踪器、记录器、格式化器等。

以下是一个使用`tracing`库的示例代码：

```rust
use tracing::{info, span, Level, Subscriber};
use tracing_subscriber::fmt;

fn main() {
    let subscriber = tracing_subscriber::registry()
        .with(fmt::layer())
        .with(
            span::Subscriber::new()
                .with_filter(Level::INFO)
                .with_span_events(span::Events::NEW_SPAN | span::Events::CLOSE),
        );
    tracing::subscriber::set_global_default(subscriber).expect("setting default subscriber failed");

    let span = span!(Level::INFO, "my_span", key1 = 1, key2 = "hello");
    let _enter = span.enter();

    info!("Hello, world!");
}
```

在这个示例中，我们使用`tracing`库来创建一个跟踪器，该跟踪器使用`fmt`格式化器来记录日志。我们首先创建一个`Subscriber`对象，然后使用`set_global_default`方法将其设置为全局默认的跟踪器。然后，我们创建一个`span`对象，并在其中记录一些信息。

在 Rust 中，`use` 关键字用于引入外部库或模块中的项到当前的作用域内。对于 `tracing` 和 `tracing_subscriber` 这两个库而言，使用 `::` 是为了指定从这些库中导入特定的组件。下面我们将详细解释所提供的代码片段，并探讨 `::` 的用法。

### 代码解析

```rust
use tracing::{info, span, Level, Subscriber};
use tracing_subscriber::fmt;
```

这段代码做了以下几件事：

1. **从 `tracing` 库导入特定项**：通过 `use tracing::{...}`，我们指定了要从 `tracing` 库中导入的几个具体项，即 `info`、`span`、`Level` 和 `Subscriber`。这里的 `::` 表示我们在访问 `tracing` 模块下的子项。
   
   - `info`: 宏，用来记录信息级别的日志消息。
   - `span`: 函数，用于创建一个新的跨度（span），它代表了一段时间内的操作。
   - `Level`: 枚举类型，定义了不同级别的日志严重性，如 `TRACE`, `DEBUG`, `INFO`, `WARN`, 和 `ERROR`。
   - `Subscriber`: trait，定义了如何收集和处理由 `tracing` 发出的日志事件。

2. **从 `tracing_subscriber` 库导入 `fmt` 模块**：`use tracing_subscriber::fmt;` 行表示我们将 `fmt` 模块带入作用域。`fmt` 提供了一个方便的方式来格式化并输出日志信息到控制台或其他输出流。

### `::` 的含义

在 Rust 中，`::` 是路径分隔符，用于指示一个项目位于另一个项目的内部。例如，在 `tracing::{info, span, Level, Subscriber}` 中，`::` 表明 `info`、`span`、`Level` 和 `Subscriber` 都是 `tracing` 模块的一部分。同样地，`tracing_subscriber::fmt` 表示 `fmt` 是 `tracing_subscriber` 模块的一个子模块。

### 示例：初始化日志订阅者

接下来，我们可以展示如何使用上述导入来设置一个简单的日志记录环境：

```rust
use tracing::{info, span, Level};
use tracing_subscriber::fmt;

fn main() {
    // 初始化 fmt 订阅者，这将开始捕获所有日志事件并将它们打印到控制台上
    fmt().init();

    // 创建一个 info 级别的跨度（span）
    let my_span = span!(Level::INFO, "my_span");
    let _enter = my_span.enter(); // 进入跨度上下文

    // 在跨度内记录一条 info 级别的消息
    info!("This is an informational message within the span.");
}
```

在这个例子中，`fmt().init()` 调用了 `tracing_subscriber::fmt` 提供的方法来配置并启动一个默认的日志订阅者，该订阅者会捕捉所有的日志事件，并以一种易于阅读的方式将它们输出到标准输出（通常是终端）。而 `span!` 宏则创建了一个新的跨度，允许开发者围绕一段逻辑执行区域添加额外的上下文信息。

此外，还可以进一步自定义 `fmt` 层的行为，比如设置最大日志级别、更改时间戳格式等。例如，可以通过链式调用来调整 `fmt` 的行为：

```rust
use tracing_subscriber::fmt::format::FmtSpan;

fmt()
    .with_max_level(Level::DEBUG) // 设置最高日志级别为 DEBUG
    .with_thread_ids(true)        // 启用线程 ID 输出
    .with_target(false)           // 不显示目标（通常是模块路径）
    .with_span_events(FmtSpan::CLOSE) // 只在关闭时打印跨度事件
    .init();
```

以上就是关于 `use tracing::{info, span, Level, Subscriber}; use tracing_subscriber::fmt;` 中 `::` 用法及其相关概念的详细介绍。希望这对理解如何在 Rust 中设置和使用 `tracing` 日志系统有所帮助。如果您有任何更具体的问题或需要更多细节，请随时提问！



在Yazi项目中，`tracing`库用于跟踪和日志记录，例如在`yazi-fm`项目的`src/signals.rs`文件中，我们使用`tracing`库来记录信号处理器的日志。

```rust
use std::time::Duration;

use anyhow::Result;
use crossterm::event::{Event as CrosstermEvent, EventStream, KeyEvent, KeyEventKind};
use futures::StreamExt;
use tokio::{select, sync::{mpsc, oneshot}};
use yazi_config::MANAGER;
use yazi_shared::event::Event;

pub(super) struct Signals {
	tx: mpsc::UnboundedSender<(bool, Option<oneshot::Sender<()>>)>,
}
impl Signals {
	pub(super) fn start() -> Result<Self> {
		let (tx, rx) = mpsc::unbounded_channel();
		Self::spawn(rx)?;
		Ok(Self { tx })
	}
	pub(super) fn stop(&mut self, cb: Option<oneshot::Sender<()>>) { self.tx.send((false, cb)).ok(); }
	pub(super) fn resume(&mut self, cb: Option<oneshot::Sender<()>>) {
		self.tx.send((true, cb)).ok();
	}
	#[cfg(unix)]
	#[inline]
	fn handle_sys(n: libc::c_int) -> bool {
		use libc::{SIGCONT, SIGHUP, SIGINT, SIGQUIT, SIGSTOP, SIGTERM, SIGTSTP};
		use tracing::error;
		use yazi_proxy::{AppProxy, HIDER};
		match n {
			SIGINT => { /* ignored */ }
			SIGQUIT | SIGHUP | SIGTERM => {
				Event::Quit(Default::default()).emit();
				return false;
			}
			SIGTSTP => {
				tokio::spawn(async move {
					AppProxy::stop().await;
					if unsafe { libc::kill(0, SIGSTOP) } != 0 {
						error!("Failed to stop the process:\n{}", std::io::Error::last_os_error());
						Event::Quit(Default::default()).emit();
					}
				});
			}
			SIGCONT if HIDER.try_acquire().is_ok() => AppProxy::resume(),
			_ => {}
		}
		true
	}
	#[cfg(windows)]
	#[inline]
	fn handle_sys(_: ()) -> bool { unreachable!() }
	#[inline]
	fn handle_term(event: CrosstermEvent) {
		match event {
			CrosstermEvent::Key(key @ KeyEvent { kind: KeyEventKind::Press, .. }) => {
				Event::Key(key).emit()
			}
			CrosstermEvent::Mouse(mouse) => {
				if MANAGER.mouse_events.contains(mouse.kind.into()) {
					Event::Mouse(mouse).emit();
				}
			}
			CrosstermEvent::Paste(str) => Event::Paste(str).emit(),
			CrosstermEvent::Resize(..) => Event::Resize.emit(),
			_ => {}
		}
	}
	fn spawn(mut rx: mpsc::UnboundedReceiver<(bool, Option<oneshot::Sender<()>>)>) -> Result<()> {
		#[cfg(unix)]
		use libc::{SIGCONT, SIGHUP, SIGINT, SIGQUIT, SIGTERM, SIGTSTP};
		#[cfg(unix)]
...
```

在这个示例中，我们使用`tracing`库来记录信号处理器的日志。我们首先创建一个`Subscriber`对象，然后使用`set_global_default`方法将其设置为全局默认的跟踪器。然后，我们使用`tracing`库来记录一些信息。

这个示例展示了如何使用`tracing`库来跟踪和日志记录，从而更方便地调试和监控程序。通过使用`tracing`库，我们可以更方便地跟踪和日志记录，从而更轻松地调试和监控程序。