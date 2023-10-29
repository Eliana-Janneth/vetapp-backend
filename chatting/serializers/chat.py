from chatting.models import Chat
from rest_framework import serializers

class ChatSerializer(serializers.ModelSerializer):
    
        class Meta:
            model = Chat
            fields = '__all__'


class FarmerChatListSerializer(serializers.ModelSerializer):

        vet_name = serializers.SerializerMethodField()
        animal_name = serializers.SerializerMethodField()

        def get_vet_name(self, obj):
            return f"{obj.veterinarian.first_name} {obj.veterinarian.last_name}" if obj.veterinarian else None
        
        def get_animal_name(self, obj):
            return f"{obj.animal.name}" if obj.animal else None

        class Meta:
            model = Chat
            exclude = ('farmer','veterinarian','animal','start_time')
            depth = 1


class VetChatListSerializer(serializers.ModelSerializer):

        farmer_name = serializers.SerializerMethodField()
        animal_name = serializers.SerializerMethodField()

        def get_farmer_name(self, obj):
            return f"{obj.farmer.first_name} {obj.farmer.last_name}" if obj.farmer else None
        
        def get_animal_name(self, obj):
            return f"{obj.animal.name}" if obj.animal else None

        class Meta:
            model = Chat
            exclude = ('farmer','veterinarian','animal','start_time')
            depth = 1