import json

from channels.generic.websocket import AsyncWebsocketConsumer
from asgiref.sync import sync_to_async

from .models import RoomModel, MessageModel
from users.models import UserModel


class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_name = self.scope["url_route"]["kwargs"]["room_name"]
        self.room_group_name = "chat_%s" % self.room_name

        await self.channel_layer.group_add(self.room_group_name, self.channel_name)

        await self.accept()

    async def disconnect(self):
        await self.channel_layer.group_discard(self.room_group_name, self.channel_name)

    async def receive(self, text_data):
        data = json.loads(text_data)

        message = data["message"]
        useremail = data["useremail"]
        room = data["room"]

        await self.save_message(useremail, room, message)

        await self.channel_layer.group_send(
            self.room_group_name,
            {
                "type": "chat_message",
                "message": message,
                "useremail": useremail,
                "room": room,
            },
        )

    async def chat_message(self, event):
        message = event["message"]
        useremail = event["useremail"]
        room = event["room"]

        await self.send(
            text_data=json.dumps(
                {
                    "message": message,
                    "useremail": useremail,
                    "room": room,
                }
            )
        )
    
    @sync_to_async
    def save_message(self, useremail, room, message):
        user = UserModel.objects.get(email=useremail)
        room = RoomModel.objects.get(slug=room)

        MessageModel.objects.create(user=user, room=room, content=message)
