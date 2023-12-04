from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
    first_name = serializers.CharField(required=True, max_length=40, min_length=2, error_messages={
        'required': 'El nombre es requerido',
        'min_length': 'El nombre debe tener mínimo 2 caracteres',
        'max_length': 'El nombre debe tener máximo 40 caracteres',
        'invalid': 'El nombre no es válido'
    })
    last_name = serializers.CharField(required=True, max_length=40, min_length=2, error_messages={
        'required': 'El apellido es requerido',
        'min_length': 'El apellido debe tener mínimo 2 caracteres',
        'max_length': 'El apellido debe tener máximo 40 caracteres',
        'invalid': 'El apellido no es válido'
    })
    document_number = serializers.CharField(
        required=True, min_length=4, max_length=20, error_messages={
            'required': 'El número de documento es requerido',
            'min_length': 'El número de documento debe tener mínimo 4 caracteres',
            'max_length': 'El número de documento debe tener máximo 20 caracteres',
            'invalid': 'El número de documento no es válido'
        })
    username = serializers.CharField(
        required=False, max_length=50, min_length=4, write_only=True, error_messages={
            'min_length': 'El nombre de usuario debe tener mínimo 4 caracteres',
            'max_length': 'El nombre de usuario debe tener máximo 50 caracteres',
            'invalid': 'El nombre de usuario no es válido'
        })
    email = serializers.EmailField(
        required=True, max_length=50, min_length=10, error_messages={
            'required': 'El correo electrónico es requerido',
            'min_length': 'El correo electrónico debe tener mínimo 4 caracteres',
            'max_length': 'El correo electrónico debe tener máximo 50 caracteres',
            'invalid': 'El correo electrónico no es válido'
        })
    password = serializers.CharField(required=True, max_length=200, min_length=8, write_only=True, error_messages={
        'required': 'La contraseña es requerida',
        'min_length': 'La contraseña debe tener mínimo 8 caracteres',
        'max_length': 'La contraseña debe tener máximo 40 caracteres',
        'invalid': 'La contraseña no es válida'
    })
    phone_number = serializers.CharField(required=True, max_length=15, min_length=7, error_messages={
        'required': 'El número de teléfono es requerido',
        'min_length': 'El número de teléfono debe tener mínimo 7 caracteres',
        'max_length': 'El número de teléfono debe tener máximo 15 caracteres',
        'invalid': 'El número de teléfono no es válido'
    })
    address = serializers.CharField(required=True, max_length=100, min_length=5, error_messages={
        'required': 'La dirección es requerida',
        'min_length': 'La dirección debe tener mínimo 5 caracteres',
        'max_length': 'La dirección debe tener máximo 100 caracteres',
        'invalid': 'La dirección no es válida'
    })
    city = serializers.CharField(required=True, max_length=50, min_length=3, error_messages={
        'required': 'La ciudad es requerida',
        'min_length': 'La ciudad debe tener mínimo 3 caracteres',
        'max_length': 'La ciudad debe tener máximo 50 caracteres',
        'invalid': 'La ciudad no es válida'
    })
    repeat_password = serializers.CharField(required=True, max_length=200, min_length=8, write_only=True, error_messages={
        'required': 'La confirmación de contraseña es requerida',
        'min_length': 'La confirmación de contraseña debe tener mínimo 8 caracteres',
        'max_length': 'La confirmación de contraseña debe tener máximo 40 caracteres',
        'invalid': 'La confirmación de contraseña no es válida'
    })