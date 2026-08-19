use pumpkin_plugin_api::{Context, Plugin, PluginMetadata};
use tracing::*;

struct BufferServer;
impl Plugin for BufferServer {
    fn new() -> Self {
        BufferServer
    }

    fn metadata(&self) -> PluginMetadata {
        PluginMetadata {
            name: "Kheremara Buffer Server".into(),
            version: env!("CARGO_PKG_VERSION").into(),
            authors: vec!["Bjorn".into()],
            description: "A simple example plugin".into(),
            permissions: vec![],
            dependencies: vec![],
        }
    }

    fn on_load(&mut self, _context: Context) -> pumpkin_plugin_api::Result<()> {
        info!("Hello from the example plugin!");
        Ok(())
    }

    fn on_unload(&mut self, _context: Context) -> pumpkin_plugin_api::Result<()> {
        info!("Example plugin unloaded. Goodbye!");
        Ok(())
    }
}

pumpkin_plugin_api::register_plugin!(BufferServer);