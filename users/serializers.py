from rest_framework import serializers
from users.models import Farmer, Veterinarian
from django.contrib.auth.hashers import make_password


class FarmerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Farmer
        exclude = ['id', 'is_superuser', 'is_staff', 'is_active',
                   'groups', 'user_permissions', 'last_login', 'date_joined']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        validated_data['password'] = make_password(validated_data['password'])
        return super(FarmerSerializer, self).create(validated_data)


class VeterinarianSerializer(serializers.ModelSerializer):
    class Meta:
        model = Veterinarian
        exclude = ['is_superuser', 'is_staff', 'is_active',
                   'groups', 'user_permissions', 'last_login', 'date_joined']
        extra_kwargs = {'password': {'write_only': True}}
    
    def create(self, validated_data):
        validated_data['password'] = make_password(validated_data['password'])
        return super(VeterinarianSerializer, self).create(validated_data)