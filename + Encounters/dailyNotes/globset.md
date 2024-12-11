在Yazi项目中，`globset`库被用作依赖项，可以在`Cargo.toml`文件中找到。这个库是一个用于处理文件路径模式匹配的库，支持通配符、正则表达式和递归匹配等功能。

以下是一个使用`globset`库的示例代码：

```rust
use globset::{Glob, GlobSetBuilder};

fn main() {
    let globset = GlobSetBuilder::new()
        .add(Glob::new("*.rs").unwrap())
        .build()
        .unwrap();

    let paths = vec!["main.rs", "foo.rs", "bar.txt"];

    for path in paths {
        if globset.is_match(path) {
            println!("Matched: {}", path);
        } else {
            println!("Not matched: {}", path);
        }
    }
}
```

在这个示例中，我们使用`globset`库来创建一个`GlobSet`，然后使用这个`GlobSet`来匹配文件路径。如果文件路径匹配成功，我们打印出"Matched"，否则打印出"Not matched"。

在Yazi项目中，`globset`库用于处理文件路径模式匹配，例如在`yazi-config`项目的`src/pattern.rs`文件中，我们使用`globset`库来解析文件路径模式，并生成相应的`Pattern`。

```rust
use std::{path::Path, str::FromStr};

use globset::GlobBuilder;
use serde::Deserialize;
#[derive(Debug, Deserialize)]
#[serde(try_from = "String")]
pub struct Pattern {
	inner:   globset::GlobMatcher,
	is_dir:  bool,
	is_star: bool,
	#[cfg(windows)]
	sep_lit: bool,
}
impl Pattern {
	#[inline]
	pub fn match_mime(&self, mime: impl AsRef<str>) -> bool {
		self.is_star || (!mime.as_ref().is_empty() && self.inner.is_match(mime.as_ref()))
	}
	#[inline]
	pub fn match_path(&self, path: impl AsRef<Path>, is_dir: bool) -> bool {
		if is_dir != self.is_dir {
			return false;
		} else if self.is_star {
			return true;
		}
		#[cfg(windows)]
		let path = if self.sep_lit {
			yazi_shared::fs::backslash_to_slash(path.as_ref())
		} else {
			std::borrow::Cow::Borrowed(path.as_ref())
		};
		self.inner.is_match(path)
	}
	#[inline]
	pub fn any_file(&self) -> bool { self.is_star && !self.is_dir }
	#[inline]
	pub fn any_dir(&self) -> bool { self.is_star && self.is_dir }
}
impl FromStr for Pattern {
	type Err = globset::Error;
	fn from_str(s: &str) -> Result<Self, Self::Err> {
		let a = s.trim_start_matches("\\s");
		let b = a.trim_end_matches('/');
		let sep_lit = b.contains('/');
		let inner = GlobBuilder::new(b)
			.case_insensitive(a.len() == s.len())
			.literal_separator(sep_lit)
			.backslash_escape(false)
			.empty_alternates(true)
			.build()?
			.compile_matcher();
		Ok(Self {
			inner,
			is_dir: b.len() < a.len(),
			is_star: b == "*",
			#[cfg(windows)]
			sep_lit,
		})
	}
}
impl TryFrom<String> for Pattern {
	type Error = globset::Error;
	fn try_from(s: String) -> Result<Self, Self::Error> { Self::from_str(s.as_str()) }
}
#[cfg(test)]
mod tests {
	use super::*;
	fn matches(glob: &str, path: &str) -> bool {
		Pattern::from_str(glob).unwrap().match_path(path, false)
	}
	#[cfg(unix)]
	#[test]
	fn test_unix() {
		// Wildcard
		assert!(matches("*", "/foo"));
		assert!(matches("*", "/foo/bar"));
		assert!(matches("**", "foo"));
		assert!(matches("**", "/foo"));
		assert!(matches("**", "/foo/bar"));
		// Filename
		assert!(matches("*.md", "foo.md"));
		assert!(matches("*.md", "/foo.md"));
...
```

在这个示例中，我们使用`globset`库来解析文件路径模式，并生成相应的`Pattern`。然后，我们使用这个`Pattern`来匹配文件路径，并返回匹配结果。

这个示例展示了如何使用`globset`库来处理文件路径模式匹配，并生成相应的`Pattern`。通过使用`globset`库，我们可以更方便地处理文件路径模式匹配，并生成相应的`Pattern`，从而更轻松地管理文件路径。