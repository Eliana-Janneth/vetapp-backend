from medical_history.models import Veterinary_Consultations
from rest_framework import serializers

class VeterinaryConsultationsSerializer(serializers.ModelSerializer):

    diagnosis = serializers.CharField(max_length=2048)
    treatment = serializers.CharField(max_length=2048)
    class Meta:
        model = Veterinary_Consultations
        exclude = ['id', 'create_date']
