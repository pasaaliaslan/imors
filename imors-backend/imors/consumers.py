# import json
import time

from channels.generic.websocket import AsyncWebsocketConsumer


class ImorsConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()

    async def disconnect(self, close_code):
        pass

    async def receive(self, text_data):
        # text_data_json = json.loads(text_data)
        # message = text_data_json["message"]
        # await self.send(text_data=json.dumps({"message": message}))

        i = 0

        while True:
            await self.send(text_data=str(i))
            i = i + 1
            time.sleep(2)
