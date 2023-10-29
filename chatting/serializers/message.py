from chatting.models import Message
from rest_framework import serializers

class MessageSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Message
        exclude = ('chat',)
        read_only_fields = ('sender','id')

class MessageDetailSerializer(serializers.ModelSerializer):
        sender_name = serializers.SerializerMethodField()
        sender_role = serializers.SerializerMethodField()


        def get_sender_name(self, obj):
            return f"{obj.sender.first_name} {obj.sender.last_name}" if obj.sender else None
        
        def get_sender_role(self, obj):
            return f"{obj.sender.role}" if obj.sender else None
        
        class Meta:
            model = Message
            exclude = ('chat','sender',)
            depth = 1
