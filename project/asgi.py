"""
ASGI config for project project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/howto/deployment/asgi/
"""

import os

from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.security.websocket import AllowedHostsOriginValidator
from django.core.asgi import get_asgi_application

import home.routing

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "project.settings")

django_asgi_app = get_asgi_application()

# ProtocolTypeRouter inspects the connection type
application = ProtocolTypeRouter(
    {
        "http": django_asgi_app,
        # if it's ws, it routes to AuthMiddlewareStack
        # which populates the scope with the currently authenticated user
        "websocket": AllowedHostsOriginValidator(
            # URLRouter inspects the HTTP path of the connection to route to
            # the correct consumer
            AuthMiddlewareStack(URLRouter(home.routing.websocket_urlpatterns))
        ),
    }
)
