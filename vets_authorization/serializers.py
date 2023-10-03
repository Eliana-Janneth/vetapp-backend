from rest_framework import serializers
from vets_authorization.models import Authorization

class VetAuthorizationSerializer(serializers.ModelSerializer):
    model = Authorization
    
