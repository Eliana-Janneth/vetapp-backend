import base64
import json
import secrets
from datetime import datetime

from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer
from django.core.files.base import ContentFile
from django.shortcuts import get_object_or_404

from users.models import Farmer, Veterinarian, User
from chatting.models import Message, Chat
from chatting.serializers.message import MessageSerializer
from chatting.serializers.chat import ChatSerializer


class ChatConsumer(WebsocketConsumer):
    
    def connect(self):
        print("here")
        self.room_name = self.scope["url_route"]["kwargs"]["room_name"]
        chat = get_object_or_404(Chat, id=self.room_name)
        user = self.scope["user"].id
        print(user)
        print(chat.farmer.id)
        print(chat.veterinarian.id)
        if (user == chat.farmer.id) or (user == chat.veterinarian.id):
            print("if")
            self.room_group_name = f"chat_{self.room_name}"
            async_to_sync(self.channel_layer.group_add)(self.room_group_name, self.channel_name)
            self.accept()
        else:
            self.room_group_name = "0"
            self.close(code=404)
            

    def disconnect(self, close_code):
        async_to_sync(self.channel_layer.group_discard)(
            self.room_group_name, self.channel_name
        )

    def receive(self, text_data=None, bytes_data=None):
        text_data_json = json.loads(text_data)
        chat_type = {"type": "chat_message"}
        return_dict = {**chat_type, **text_data_json}
        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name,
            return_dict,
        )

    def chat_message(self, event):
        text_data_json = event.copy()
        text_data_json.pop("type")
        message, attachment = (
            text_data_json["message"],
            text_data_json.get("attachment"),
        )
        chat = Chat.objects.get(id=int(self.room_name))
        sender = self.scope['user']
        if attachment:
            file_str, file_ext = attachment["data"], attachment["format"]
            file_data = ContentFile(
                base64.b64decode(file_str), name=f"{secrets.token_hex(8)}.{file_ext}"
            )
            _message = Message.objects.create(
                sender=sender,
                file=file_data,
                message=message,
                chat=chat,
            )
        else:
            _message = Message.objects.create(
                sender=sender,
                message=message,
                chat=chat,
            )
        serializer = MessageSerializer(instance=_message)
        self.send(
            text_data=json.dumps(
                serializer.data
            )
        )