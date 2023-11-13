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
        fields = '__all__'


class MedicalHistoryUpdateSerializer(serializers.ModelSerializer):
    diagnosis = serializers.CharField(max_length=2048, required=False, error_messages={
        'max_length': 'El diagnóstico no puede tener más de 2048 caracteres',
    })
    treatment = serializers.CharField(max_length=2048, required=False, error_messages={
        'max_length': 'El tratamiento no puede tener más de 2048 caracteres',
    })
    
    class Meta:
        model = MedicalHistory
        exclude = ('veterinarian', 'animal')
        read_only_fields = ('veterinarian', 'animal', 'create_date', 'id')

class MedicalHistoryBaseSerializer(serializers.ModelSerializer):
    vet_name = serializers.SerializerMethodField()
    def get_vet_name(self, obj):
        return f"{obj.veterinarian.first_name} {obj.veterinarian.last_name}" if obj.veterinarian else None
    
    class Meta:
        model = MedicalHistory
        exclude = ['veterinarian', 'animal']
        read_only_fields = ('veterinarian', 'animal', 'create_date', 'update_date', 'diagnosis', 'treatment', 'id')
    

class MedicalHistoryVetSerializer(MedicalHistoryBaseSerializer):
    can_modify = serializers.SerializerMethodField()
    
    def get_can_modify(self, obj):
        print(self.context['vet'])
        print(obj.veterinarian.id)
        return True if obj.veterinarian.id == self.context['vet'] else False
    
    class Meta:
        model = MedicalHistory
        exclude = ['veterinarian', 'animal']
        read_only_fields = ('veterinarian', 'animal', 'create_date', 'update_date', 'diagnosis', 'treatment', 'id')
