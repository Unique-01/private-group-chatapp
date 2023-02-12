from group_chat.consumers import GroupChatConsumer
from django.urls import path,re_path

websocket_urlpatterns = [
    re_path(r'^ws/chat/(?P<room_name>[^/]+)/$',GroupChatConsumer.as_asgi())
]