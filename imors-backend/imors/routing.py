from django.urls import re_path

from . import consumers

websocket_urlpatterns = [
    re_path(r"ws/download_video/$", consumers.ImorsConsumer.as_asgi()),
]
