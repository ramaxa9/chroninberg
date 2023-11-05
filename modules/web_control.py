import asyncio

from PySide6.QtCore import QThread, Signal, QObject
from aiohttp import web


class SignalHandler(QObject):
    cmd_start = Signal()
    cmd_reset = Signal()
    cmd_pause = Signal()
    cmd_setTime = Signal(int)


class CommandHandler:
    def __init__(self):
        self.loop = asyncio.new_event_loop()
        asyncio.set_event_loop(self.loop)

        self.app = web.Application()
        self.app.router.add_post('/start', self.command_start)
        self.app.router.add_post('/reset', self.command_reset)
        self.app.router.add_post('/set_timer', self.command_set_timer)

        self.signal_handler = SignalHandler()

    async def command_set_timer(self, request):
        time = request.query.get('time')

        msg = f'[NETWORK] set timer to {time}m'
        print(msg)
        feedback = msg

        self.signal_handler.cmd_setTime.emit(int(time))
        return web.Response(text=feedback)

    async def command_start(self, request):
        msg = '[NETWORK] start timer'
        print(msg)
        feedback = msg

        self.signal_handler.cmd_start.emit()
        return web.Response(text=feedback)

    async def command_reset(self, request):
        msg = '[NETWORK] reset timer'
        print(msg)
        feedback = msg

        self.signal_handler.cmd_reset.emit()
        return web.Response(text=feedback)

    def start_server(self):
        web.run_app(self.app, port=5000)

    def stop_server(self):
        self.loop.call_soon_threadsafe(self.loop.stop)


class ServerThread(QThread):
    started = Signal()
    finished = Signal()

    def __init__(self, command_handler):
        super().__init__()
        self.command_handler = command_handler

    def run(self):
        self.started.emit()
        self.command_handler.start_server()
        self.finished.emit()