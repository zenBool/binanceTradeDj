from django.urls import path

from .consumers import WSConsumerMonitor


ws_urlpatterns = [
    path('ws/monitor/', WSConsumerMonitor.as_asgi())
]