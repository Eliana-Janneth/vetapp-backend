from rest_framework import serializers
from users.models import Veterinarian
from django.contrib.auth.hashers import make_password
from users.serializers.user_serializer import UserSerializer

class VeterinarianSerializer(UserSerializer):
    license_number = serializers.CharField(required=False, allow_null = True, max_length=20, min_length=4, error_messages={
        'required': 'El número de licencia es requerido',
        'min_length': 'El número de licencia debe tener mínimo 4 caracteres',
        'max_length': 'El número de licencia debe tener máximo 20 caracteres',
        'invalid': 'El número de licencia no es válido'
    })
    license_expiry_date = serializers.DateField(required=False, allow_null = True,error_messages={
        'required': 'La fecha de expiración de la licencia es requerida',
        'invalid': 'La fecha de expiración de la licencia no es válida'
    })
    available = serializers.BooleanField(required=False)


    class Meta:
        model = Veterinarian
        exclude = ['id', 'is_superuser', 'is_staff', 'is_active',
                   'groups', 'user_permissions', 'last_login', 'date_joined']
        read_only_fields = ['role']

    def create(self, validated_data):
        validated_data['username'] = validated_data['email'].split('@')[0]
        validated_data['password'] = make_password(validated_data['password'])
        validated_data['role'] = 'veterinarian'
        validated_data.pop('repeat_password')
        return super(VeterinarianSerializer, self).create(validated_data)

    def validate(self, validated_data):
        if validated_data['password'] != validated_data['repeat_password']:
            raise serializers.ValidationError(
                {'response': 'Las contraseñas no coinciden'})
        return validated_data


class VeterinarianListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Veterinarian
        fields = ['id','first_name','last_name','city','license_number','license_expiry_date']


class VeterinarianUpdateInfoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Veterinarian
        fields = ['license_number','license_expiry_date']