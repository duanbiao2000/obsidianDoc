在Yazi项目中，`mlua`库被用作依赖项，可以在`Cargo.toml`文件中找到。这个库是一个用于在Rust中嵌入Lua脚本的库，支持异步操作。

以下是一个使用`mlua`库的示例代码：

```rust
use mlua::{Lua, Result};

fn main() -> Result<()> {
    let lua = Lua::new();
    let _ = lua.eval(r#"
        local x = 10
        local y = 20
        local z = x + y
        print(z)
    "#, None)?;
    Ok(())
}
```

在这个示例中，我们使用`mlua`库来执行一个简单的Lua脚本，该脚本计算两个数字的和并打印结果。

在Yazi项目中，`mlua`库用于嵌入Lua脚本，例如在`yazi-plugin`项目的`src/lua.rs`文件中，我们使用`mlua`库来加载和执行Lua脚本。

```rust
use anyhow::{Context, Result};
use mlua::Lua;
use yazi_boot::BOOT;
use yazi_macro::plugin_preset as preset;
use yazi_shared::RoCell;

use crate::runtime::Runtime;
pub static LUA: RoCell<Lua> = RoCell::new();
pub(super) fn init_lua() -> Result<()> {
	LUA.init(Lua::new());
	stage_1(&LUA).context("Lua setup failed")?;
	stage_2(&LUA).context("Lua runtime failed")?;
	Ok(())
}
fn stage_1(lua: &'static Lua) -> Result<()> {
	lua.set_named_registry_value("rt", Runtime::default())?;
	crate::Config::new(lua).install_boot()?.install_manager()?.install_theme()?;
	// Base
	let globals = lua.globals();
	globals.raw_set("ui", crate::elements::compose(lua)?)?;
	globals.raw_set("ya", crate::utils::compose(lua, false)?)?;
	globals.raw_set("ps", crate::pubsub::compose(lua)?)?;
	crate::Error::install(lua)?;
	crate::bindings::Cha::install(lua)?;
	crate::loader::install(lua)?;
	crate::file::pour(lua)?;
	crate::url::pour(lua)?;
	// Addons
	lua.load(preset!("ya")).set_name("ya.lua").exec()?;
	// Components
	lua.load(preset!("components/current")).set_name("current.lua").exec()?;
	lua.load(preset!("components/entity")).set_name("entity.lua").exec()?;
	lua.load(preset!("components/header")).set_name("header.lua").exec()?;
	lua.load(preset!("components/linemode")).set_name("linemode.lua").exec()?;
	lua.load(preset!("components/marker")).set_name("marker.lua").exec()?;
	lua.load(preset!("components/parent")).set_name("parent.lua").exec()?;
	lua.load(preset!("components/preview")).set_name("preview.lua").exec()?;
	lua.load(preset!("components/progress")).set_name("progress.lua").exec()?;
	lua.load(preset!("components/rail")).set_name("rail.lua").exec()?;
	lua.load(preset!("components/root")).set_name("root.lua").exec()?;
	lua.load(preset!("components/status")).set_name("status.lua").exec()?;
	lua.load(preset!("components/tab")).set_name("tab.lua").exec()?;
	Ok(())
}
fn stage_2(lua: &'static Lua) -> mlua::Result<()> {
	lua.load(preset!("setup")).set_name("setup.lua").exec()?;
	lua.load(preset!("compat")).set_name("compat.lua").exec()?;
	Ok(())
}
```

在这个示例中，我们使用`mlua`库来加载和执行Lua脚本，这些脚本用于设置和初始化Lua环境，并加载和执行一些Lua组件。

这个示例展示了如何使用`mlua`库来嵌入和执行Lua脚本，从而在Rust中嵌入Lua脚本。通过使用`mlua`库，我们可以更方便地Rust中嵌入Lua脚本，从而实现更灵活和强大的扩展的功能。