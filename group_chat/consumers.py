from channels.generic.websocket import AsyncWebsocketConsumer
import json
from channels.db import database_sync_to_async
from .models import RoomMessage, Room
from django.contrib.auth.models import User
from asgiref.sync import sync_to_async, async_to_sync


class GroupChatConsumer(AsyncWebsocketConsumer):
    @database_sync_to_async
    def save_message(self, sender, content, room_name):
        room = Room.objects.get(room_name=room_name)
        msg = RoomMessage.objects.create(sender=sender, content=content, room=room)
        msg.save()

    async def connect(self):
        self.room_name = self.scope["url_route"]["kwargs"]["room_name"]
        self.room_group_name = "chat_%s" % self.room_name
        self.user = self.scope["user"]

        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name,
        )

        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name,
        )

    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        username = text_data_json["username"]
        message = text_data_json["message"]

        await self.save_message(
            sender=self.scope["user"], content=message, room_name=self.room_name
        )

        await self.channel_layer.group_send(
            self.room_group_name,
            {"type": "roomMessage", "username": username, "message": message},
        )

    async def roomMessage(self, event):
        username = event["username"]
        message = event["message"]

        await self.send(
            text_data=json.dumps({"username": username, "message": message})
        )
