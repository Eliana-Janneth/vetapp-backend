"""
ASGI config for vetapp project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/asgi/
"""

import os

from channels.routing import URLRouter, ProtocolTypeRouter
from django.core.asgi import get_asgi_application
from channels.security.websocket import AllowedHostsOriginValidator
from chatting.knox_middleware import TokenAuthMiddleware
from chatting.routing import websocket_urlpatterns as routing


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'vetapp.settings')
application = ProtocolTypeRouter({
    "http": get_asgi_application(),
    "websocket": AllowedHostsOriginValidator(  
        TokenAuthMiddleware(URLRouter(routing)))
})