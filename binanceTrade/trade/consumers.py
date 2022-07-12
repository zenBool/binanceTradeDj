import json
from time import sleep
from random import randint

from channels.generic.websocket import WebsocketConsumer


class WSConsumerMonitor(WebsocketConsumer):
    def connect(self):
        self.accept()

        for i in range(100):
            self.send(json.dumps({'message': randint(1, i+1)}))
            sleep(1)

