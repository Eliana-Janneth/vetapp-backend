from rest_framework import serializers
from users.models import Farmer, Veterinarian
from django.contrib.auth.hashers import make_password


class FarmerSerializer(serializers.ModelSerializer):
    username = serializers.CharField(required=True, max_length=50, min_length=4)
    email = serializers.EmailField(required=True)
    document_number = serializers.CharField(required=True)
    phone_number = serializers.CharField(required=True)
    password = serializers.CharField(required=True)

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
        exclude = ['licence_number','license_expiry_date','is_superuser', 'is_staff', 'is_active',
                   'groups', 'user_permissions', 'last_login', 'date_joined']
        extra_kwargs = {'password': {'write_only': True}}
    
    def create(self, validated_data):
        validated_data['password'] = make_password(validated_data['password'])
        return super(VeterinarianSerializer, self).create(validated_data)