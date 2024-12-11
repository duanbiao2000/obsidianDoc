在Yazi项目中，`uzers`库被用作依赖项，可以在`Cargo.toml`文件中找到。这个库是一个用于处理用户和权限的库，它提供了一套完整的用户和权限管理功能，包括用户信息获取、权限检查等。

以下是一个使用`uzers`库的示例代码：

```rust
use uzers::Users;

fn main() {
    let users = Users::new();
    let user = users.get_user_by_uid(1000).unwrap();
    println!("User name: {}", user.name());
}
```

在这个示例中，我们使用`uzers`库来获取用户信息。我们首先创建一个`Users`对象，然后使用`get_user_by_uid`方法来获取用户信息。

在Yazi项目中，`uzers`库用于处理用户和权限，例如在`yazi-fm`项目的`src/signals.rs`文件中，我们使用`uzers`库来获取当前用户的用户名。

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

在这个示例中，我们使用`uzers`库来获取当前用户的用户名。我们首先创建一个`Users`对象，然后使用`get_user_by_uid`方法来获取当前用户的用户名。

这个示例展示了如何使用`uzers`库来处理用户和权限，从而更方便地管理和监控用户。通过使用`uzers`库，我们可以更方便地管理和监控用户，从而更轻松地调试和监控程序。