from group_chat.consumers import GroupChatConsumer
from private_chat.consumers import PrivateChatConsumer
from django.urls import re_path

websocket_urlpatterns = [
    re_path(r"^ws/roomchat/(?P<room_name>[^/]+)/$", GroupChatConsumer.as_asgi()),
    re_path(r"^ws/privatechat/(?P<username>[^/]+)/$", PrivateChatConsumer.as_asgi()),
]
