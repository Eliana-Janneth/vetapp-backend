from users.models import User
from rest_framework import serializers


class UserMixin:
    def check_users_exists(self, validated_data):
        email = validated_data['email']
        document_number = validated_data['document_number']
        if User.objects.filter(email=email).exists():
            raise serializers.ValidationError(
                {'response': 'Ya existe un usuario registrado con este correo'})
        if User.objects.filter(document_number=document_number):
            raise serializers.ValidationError(
                {'response': 'Ya existe un usuario registrado con este número de documento'})
