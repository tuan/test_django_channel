from django.urls import re_path

from . import consumers

websocket_urlpatterns = [
    # as_asgi() returns ASGI app that instantiates an instance of ChatConsumer
    # for each user connection
    re_path(r"ws/chat/(?P<room_name>\w+)/$", consumers.ChatConsumer.as_asgi()),
]
