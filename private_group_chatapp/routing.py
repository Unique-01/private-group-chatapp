from group_chat.consumers import GroupChatConsumer
from django.urls import path,re_path

websocket_urlpatterns = [
    path('',GroupChatConsumer.as_asgi(),)
]