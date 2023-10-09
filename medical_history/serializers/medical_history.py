from medical_history.models import MedicalHistory
from rest_framework import serializers
from animals.models import Animals
from users.models import Veterinarian
class MedicalHistorySerializer(serializers.ModelSerializer):
    veterinarian = serializers.PrimaryKeyRelatedField(
        required=True, queryset=Veterinarian.objects.all(), write_only=True, error_messages={
            'required': 'El veterinario es requerido',
            'does_not_exist': 'El veterinario especificado no existe',
            'incorrect_type': 'El veterinario debe ser un número entero',
        })
    animal = serializers.PrimaryKeyRelatedField(
        required=True, queryset=Animals.objects.all(), write_only=True, error_messages={
            'required': 'El animal es requerido',
            'does_not_exist': 'El animal especificado no existe',
            'incorrect_type': 'El animal debe ser un número entero',
        })
    diagnosis = serializers.CharField(max_length=2048, required=True, error_messages={
        'required': 'Por favor, ingrese un diagnóstico',
        'max_length': 'El diagnóstico no puede tener más de 2048 caracteres',
    })
    treatment = serializers.CharField(max_length=2048, required=True, error_messages={
        'required': 'Por favor, ingrese un tratamiento',
        'max_length': 'El tratamiento no puede tener más de 2048 caracteres',
    })
    class Meta:
        model = MedicalHistory
        exclude = ['id']
