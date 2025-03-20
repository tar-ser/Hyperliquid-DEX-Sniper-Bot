import websockets
import asyncio
from typing import Callable

class DataFeed:
    def __init__(self, ws_url: str):
        self.ws_url = ws_url
        self._callbacks = []
        
    def add_callback(self, callback: Callable):
        self._callbacks.append(callback)
        
    async def _listen(self):
        async with websockets.connect(self.ws_url) as ws:
            while True:
                try:
                    data = await ws.recv()
                    for cb in self._callbacks:
                        await cb(json.loads(data))
                except websockets.ConnectionClosed:
                    await asyncio.sleep(5)
                    self._reconnect()
                    
    def _reconnect(self):
        print("Reconnecting to data feed...")
        asyncio.create_task(self._listen())

    def start(self):
        asyncio.run(self._listen())
