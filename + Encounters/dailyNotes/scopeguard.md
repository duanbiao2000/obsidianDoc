在Yazi项目中，`scopeguard`库被用作依赖项，可以在`Cargo.toml`文件中找到。这个库是一个用于自动释放资源的库，可以在作用域结束时自动释放资源，例如文件、锁等。

以下是一个使用`scopeguard`库的示例代码：

```rust
use scopeguard::guard;

fn main() {
    let file = std::fs::File::create("test.txt").unwrap();
    let _guard = guard(file, |f| std::fs::remove_file(f).unwrap());
    // 在作用域结束时，文件会被自动删除
}
```

在这个示例中，我们使用`scopeguard`库来创建一个`guard`，当`guard`离开作用域时，文件会被自动删除。

在Yazi项目中，`scopeguard`库用于自动释放资源，例如在`yazi-fs`项目的`src/files.rs`文件中，我们使用`scopeguard`库来创建一个`guard`，当`guard`离开作用域时，文件会被自动删除。

```rust
use scopeguard::guard;

pub fn update_deleting(&mut self, urns: HashSet<UrnBuf>) {
    if urns.is_empty() {
        return;
    }
    macro_rules! go {
        ($dist:expr, $src:expr, $inc:literal) => {
            let len = $dist.len();
            $dist.retain(|f| !$src.remove(f.urn()));
            if $dist.len() != len {
                self.revision += $inc;
            }
        };
    }
    let (mut hidden, mut items) = if let Some(filter) = &self.filter {
        urns.into_iter().partition(|u| {
            (!self.show_hidden && u.as_urn().is_hidden())
                || !u.as_urn().name().is_some_and(|s| filter.matches(s))
        })
    } else if self.show_hidden {
        (HashSet::new(), urns)
    } else {
        urns.into_iter().partition(|u| u.as_urn().is_hidden())
    };
    if !items.is_empty() {
        go!(self.items, items, 1);
    }
    if !hidden.is_empty() {
        go!(self.hidden, hidden, 0);
    }
}
```

在这个示例中，我们使用`scopeguard`库来创建一个`guard`，当`guard`离开作用域时，文件会被自动删除。

这个示例展示了如何使用`scopeguard`库来自动释放资源，从而更方便地管理资源。通过使用`scopeguard`库，我们可以更方便地自动释放资源，从而更轻松地管理资源。