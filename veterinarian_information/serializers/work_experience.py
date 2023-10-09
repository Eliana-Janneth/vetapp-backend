from rest_framework import serializers
from veterinarian_information.models import Work_Experience

class WorkExperienceSerializer(serializers.ModelSerializer):
    title = serializers.CharField(max_length=256, required=True, error_messages={
        'required': 'Por favor, ingrese un título',
        'max_length': 'El título no puede tener más de 256 caracteres'
        })
    company = serializers.CharField(max_length=100, required=True, error_messages={
        'required': 'Por favor, ingrese una empresa',
        'max_length': 'La empresa no puede tener más de 100 caracteres'
        })
    functions = serializers.CharField(max_length=256, required=True, error_messages={
        'required': 'Por favor, ingrese sus funciones',
        'max_length': 'Las funciones no puede tener más de 256 caracteres'
        })
    start_date = serializers.DateField(required=True, error_messages={
        'invalid': 'La fecha de inicio debe tener el formato YYYY-MM-DD',
        'required': 'Por favor, ingrese una fecha de inicio'
        })
    end_date = serializers.DateField(required=False, error_messages={
        'invalid': 'La fecha de finalización debe tener el formato YYYY-MM-DD'
        })
    country = serializers.CharField(max_length=32, required=True, error_messages={
        'required': 'Por favor, ingrese un país',
        'max_length': 'El país no puede tener más de 32 caracteres'
        })
    currently_working = serializers.BooleanField(required=False, write_only=True)
    currently = serializers.SerializerMethodField()

    class Meta:
        model = Work_Experience
        exclude = ['id', 'added_time', 'update_time']

    def get_currently(self, obj):
        print(obj.currently_working)
        return "Actualidad" if obj.currently_working else "Finalizado"