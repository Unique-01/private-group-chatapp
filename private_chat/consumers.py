from channels.generic.websocket import AsyncJsonWebsocketConsumer
import json
from channels.db import database_sync_to_async
from .models import PrivateMessage
import datetime


class PrivateChatConsumer(AsyncJsonWebsocketConsumer):
    @database_sync_to_async
    def save_message(self,sender,room,content):
        msg = PrivateMessage.objects.create(sender=sender,room=room,content=content)
        msg.save()


    async def connect(self):
        user1 = self.scope["url_route"]["kwargs"]["username"]
        user2 = self.scope["user"].username

        user_list = [user1, user2]

        user_list.sort()
        user_list = "".join(user_list)
        self.room_name = user_list
        self.room_group_name = "chat_%s" % self.room_name

        await self.channel_layer.group_add(self.room_group_name, self.channel_name)

        await self.accept()

    async def disconnect(self, code):
        await self.channel_layer.group_discard(self.room_group_name, self.channel_name)

    async def receive_json(self, content):
        sender = content["sender"]
        message = content["message"]
        timestamp = datetime.datetime.now().isoformat()

        await self.save_message(sender=self.scope["user"], room=self.room_name, content=message)

        await self.channel_layer.group_send(
            self.room_group_name,
            {"type": "privateMessage", "sender": sender, "message": message,"timestamp":timestamp},
        )

    async def privateMessage(self, event):
        sender = event["sender"]
        message = event["message"]
        timestamp = event["timestamp"]
        await self.send_json({"sender": sender, "message": message,"timestamp":timestamp})
