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