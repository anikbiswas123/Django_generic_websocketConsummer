from django.urls import path 

from .consummer import *

websocket_urlpatterns=[
      path('ws/wsc/',mywebsocketConsummer.as_asgi()),
      path('ws/awsc/',myayncwebsocketConsummer.as_asgi())
]