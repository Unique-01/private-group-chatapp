"""
ASGI config for private_group_chatapp project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter,URLRouter
from channels.auth import AuthMiddlewareStack
from .routing import websocket_urlpatterns

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'private_group_chatapp.settings')

application = get_asgi_application()

application = ProtocolTypeRouter(
    {
        "http":get_asgi_application(),
        "websocket":AuthMiddlewareStack(URLRouter(
            websocket_urlpatterns)
        )
    }
)
