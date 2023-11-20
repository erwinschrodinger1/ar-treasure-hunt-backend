import json

from channels.generic.websocket import WebsocketConsumer
from django.conf import settings
import jwt

from user.models import User
from user.serializers import UserModelSerializer
from location.serializers import LocationSerializer


class LocationConsumer(WebsocketConsumer):
    def connect(self):
        try:
            token = ""
            for name, value in self.scope.get("headers", []):
                if name == b"token":
                    token = (value.decode("latin1")).split(" ")[1]
                    break
                else:
                    token = ""
            if (token):
                decodedToken = jwt.decode(
                    token, settings.SECRET_KEY, algorithms=["HS256"])
                id = (decodedToken['user_id'])
                User.objects.get(id=id)
                self.scope['session']['user_id'] = id
                self.accept()
                self.send(text_data=json.dumps({
                    "type": "connection_established",
                    "message": "You anre now connected!"
                }))

            print(token)
        except:
            self.disconnect("Invalid Credential")

    def receive(self, text_data=None, bytes_data=None):
        coordinates = json.loads(text_data)
        coordinates["user"] = self.scope['session']['user_id']
        serializer = LocationSerializer(data=coordinates)
        if serializer.is_valid():
            print("here")
            serializer.save()
        else:
            print(serializer.errors)
            self.send("fudge you")
