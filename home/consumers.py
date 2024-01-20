import json

from channels.generic.websocket import AsyncWebsocketConsumer


class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        # every consumer has a scope that has info about
        # the currently connected user, url, etc.
        self.room_name = self.scope["url_route"]["kwargs"]["room_name"]
        self.room_group_name = f"chat_{self.room_name}"

        assert self.channel_layer is not None
        # join room group
        # any consumer can join a group if they know the group's name
        await self.channel_layer.group_add(self.room_group_name, self.channel_name)

        # accept connection from client
        # normally the last action in connect()
        await self.accept()

    async def disconnect(self, close_code):
        assert self.channel_layer is not None
        # Leave room group
        await self.channel_layer.group_discard(self.room_group_name, self.channel_name)

    # Receive message from websocket
    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json["message"]

        assert self.channel_layer is not None
        # the type key, i.e. chat_message in this case, corresponds
        # to the name of the method that should be invoked on consumers that
        # receive the event
        await self.channel_layer.group_send(
            self.room_group_name, {"type": "chat_message", "message": message}
        )

    # Receive message from room group
    async def chat_message(self, event):
        message = event["message"]

        await self.send(text_data=json.dumps({"message": message}))
