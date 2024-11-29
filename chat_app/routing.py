from django.urls import re_path

from .consumers import ChatConsumer


websocket_urlpatterns = [
    # Routes to the ChatConsumer and username is URL parameters
        re_path(r'ws/chat/(?P<username>\w+)/$', ChatConsumer.as_asgi()),
    ]