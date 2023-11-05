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
from chatting.serializers.message import MessageSerializer, MessageDetailSerializer
from chatting.serializers.chat import ChatSerializer


class ChatConsumer(WebsocketConsumer):
    
    def connect(self):
        self.room_name = self.scope["url_route"]["kwargs"]["room_name"]
        chat = get_object_or_404(Chat, id=self.room_name)
        user = self.scope["user"].id
        if (user == chat.farmer.id) or (user == chat.veterinarian.id):
            self.room_group_name = f"chat_{self.room_name}"
            async_to_sync(self.channel_layer.group_add)(self.room_group_name, self.channel_name)
            self.accept()
            data = self.fetch_chat_with_messages(self.room_name)
            self.send(text_data=json.dumps(data))
        else:
            self.room_group_name = "0"
            self.close(code=404)
            

    def disconnect(self, close_code):
        async_to_sync(self.channel_layer.group_discard)(
            self.room_group_name, self.channel_name
        )

    def receive(self, text_data=None, bytes_data=None):
        text_data_json = json.loads(text_data)
        chat_type = {"type": "chat_message", "sender_id": self.scope["user"].id}  # Agregar el ID del remitente
        return_dict = {**chat_type, **text_data_json}
        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name,
            return_dict,
        )
    
    def chat_message(self, event):
        message_sender = event['sender_id']
        current_user = self.scope["user"].id
        if message_sender != current_user:
            text_data_json = event.copy()
            text_data_json.pop("type")
            text_data_json.pop("sender_id")
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
            serializer = MessageDetailSerializer(instance=_message)
            self.send(
                text_data=json.dumps(
                    serializer.data
                )
            )
    
    def fetch_chat_with_messages(self, chat_id):
        chat = Chat.objects.prefetch_related('message_set').get(id=chat_id)
        chat_serializer = ChatSerializer(chat)
        messages = chat.message_set.all()
        message_serializer = MessageDetailSerializer(messages, many=True)
        return {
            'chat': chat_serializer.data,
            'messages': message_serializer.data
        }
