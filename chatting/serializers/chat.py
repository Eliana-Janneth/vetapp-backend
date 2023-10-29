from chatting.models import Chat
from rest_framework import serializers

class ChatSerializer(serializers.ModelSerializer):
    
        class Meta:
            model = Chat
            fields = '__all__'


class ChatListSerializer(serializers.ModelSerializer):
    
        class Meta:
            model = Chat
            fields = '__all__'
            depth = 1