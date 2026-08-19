from endstone.plugin import Plugin
from pathlib import Path
from endstone import Logger, Server
from aiohttp import web
from .uptime import Uptime, format_uptime

class IpcServer:
    @property
    def _logger(self) -> Logger:
        return self._plugin.logger
    
    @property
    def _server(self) -> Server:
        return self._plugin.server

    def __init__(self, plugin: Plugin, sock_path: Path):
        self.runner = None
        self.sock_path = sock_path
        self._plugin = plugin
        self._uptime = Uptime()

    async def start(self):
        app = web.Application()
        app.router.add_post('/status', self.status)
        app.router.add_post('/shutdown', self.shutdown)
        
        self.runner = web.AppRunner(app)
        await self.runner.setup()
        
        self.sock_path.unlink(missing_ok=True)
        
        site = web.UnixSite(self.runner, self.sock_path)
        
        await site.start()
        
        self._logger.info(f"API listening on {self.sock_path}")

    async def stop(self):
        if self.runner is not None:
            await self.runner.cleanup()
        self.sock_path.unlink(missing_ok=True)
        self._logger.info("API stopped")

    async def status(self, request: web.Request) -> web.Response:
        if request.query.get("maximal", "").lower() == "true":
            return web.json_response({
                "status": "ok",
                "uptime": format_uptime(self._uptime.now),
                "tps": f"{self._server.average_tps}",
                "name": self._server.name,
                "version": self._server.version,
                "minecraft_version": self._server.minecraft_version,
                "players": f"{len(self._server.online_players)}",
                "max_players": f"{self._server.max_players}",
            })
        else:
            return web.json_response({"status": "ok"})

    async def shutdown(self, _request: web.Request) -> web.Response:
        self._server.shutdown()
        return web.json_response({"success": "true"})