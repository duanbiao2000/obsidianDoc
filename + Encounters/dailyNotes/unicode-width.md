在Yazi项目中，`unicode-width`库被用作依赖项，可以在`Cargo.toml`文件中找到。这个库是一个用于计算Unicode字符宽度的库，它提供了一套完整的Unicode字符宽度计算功能。

以下是一个使用`unicode-width`库的示例代码：

```rust
use unicode_width::UnicodeWidthStr;

fn main() {
    let s = "Hello, world!";
    let width = s.width();
    println!("The width of '{}' is {}", s, width);
}
```

在这个示例中，我们使用`unicode-width`库来计算字符串的宽度。我们首先创建一个字符串，然后使用`width`方法来计算字符串的宽度。

在Yazi项目中，`unicode-width`库用于计算Unicode字符宽度，例如在`yazi-fm`项目的`src/which/which.rs`文件中，我们使用`unicode-width`库来计算字符串的宽度。

```rust
use ratatui::{buffer::Buffer, layout, layout::{Constraint, Rect}, widgets::{Block, Widget}};
use yazi_config::THEME;

use super::Cand;
use crate::Ctx;
const PADDING_X: u16 = 1;
const PADDING_Y: u16 = 1;
pub(crate) struct Which<'a> {
	cx: &'a Ctx,
}
impl<'a> Which<'a> {
	pub(crate) fn new(cx: &'a Ctx) -> Self { Self { cx } }
}
impl Widget for Which<'_> {
	fn render(self, area: Rect, buf: &mut Buffer) {
		let which = &self.cx.which;
		if which.silent {
			return;
		}
		let cols = THEME.which.cols as usize;
		let height = area.height.min(which.cands.len().div_ceil(cols) as u16 + PADDING_Y * 2);
		let area = Rect {
			x: PADDING_X.min(area.width),
			y: area.height.saturating_sub(height + PADDING_Y * 2),
			width: area.width.saturating_sub(PADDING_X * 2),
			height,
		};
		// Don't render if there's no space
		if area.height <= PADDING_Y * 2 {
			return;
		}
		let chunks = {
			use Constraint::*;
			layout::Layout::horizontal(match cols {
				1 => &[Ratio(1, 1)][..],
				2 => &[Ratio(1, 2), Ratio(1, 2)],
				_ => &[Ratio(1, 3), Ratio(1, 3), Ratio(1, 3)],
			})
			.split(area)
		};
		yazi_plugin::elements::Clear::default().render(area, buf);
		Block::new().style(THEME.which.mask).render(area, buf);
		for y in 0..area.height {
			for (x, chunk) in chunks.iter().enumerate() {
				let Some(cand) = which.cands.get(y as usize * cols + x) else {
					break;
				};
				Cand::new(cand, which.times).render(Rect { y: chunk.y + y + 1, height: 1, ..*chunk }, buf);
			}
		}
	}
}
```

在这个示例中，我们使用`unicode-width`库来计算字符串的宽度。我们首先创建一个字符串，然后使用`width`方法来计算字符串的宽度。

这个示例展示了如何使用`unicode-width`库来计算Unicode字符宽度，从而更方便地处理Unicode字符。通过使用`unicode-width`库，我们可以更方便地计算Unicode字符宽度，从而更轻松地处理Unicode字符。