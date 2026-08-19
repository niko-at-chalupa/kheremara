from endstone.asyncio import submit
import tempfile
from endstone.plugin import Plugin
from .ipc import IpcServer
from pathlib import Path

class Reporter(Plugin):
    def on_enable(self):
        self.data_folder.mkdir(exist_ok=True)
        self.ipc_server = IpcServer(self, Path(tempfile.gettempdir()) / f"kheremara_reporter_{self.server.port}.sock")
        submit(self.ipc_server.start())

    def on_disable(self):
        submit(self.ipc_server.stop())