from rest_framework import serializers
from users.models import Farmer
from django.contrib.auth.hashers import make_password
from users.serializers.user_serializer import UserSerializer

class FarmerSerializer(UserSerializer):
    class Meta:
        model = Farmer
        exclude = ['id', 'is_superuser', 'is_staff', 'is_active',
                   'groups', 'user_permissions', 'last_login', 'date_joined']
        read_only_fields = ['role']

    def create(self, validated_data):
        validated_data['username'] = validated_data['email'].split('@')[0]
        validated_data['password'] = make_password(validated_data['password'])
        validated_data['role'] = 'farmer'
        validated_data.pop('repeat_password')
        return super(FarmerSerializer, self).create(validated_data)

    def validate(self, validated_data):
        if validated_data['password'] != validated_data['repeat_password']:
            raise serializers.ValidationError(
                {'response': 'Las contraseñas no coinciden'})
        return validated_data