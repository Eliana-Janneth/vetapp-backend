from rest_framework.response import Response
from rest_framework import status
from animals.models import Animals
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from knox.auth import TokenAuthentication
from knox.models import AuthToken
from knox.settings import CONSTANTS
from vets_authorization.models import Authorization
from animals.serializers import AnimalSerializer

# Create your views here.
def get_veterinarian(token):
        user = AuthToken.objects.get(token_key=token[:CONSTANTS.TOKEN_KEY_LENGTH])
        if not user or not user.user.role == 'veterinarian':
            return None
        return user.user

def check_authentication(request):
        if not request.headers['Authorization']:
            return Response({'response': 'No estás logueado'}, status=status.HTTP_400_BAD_REQUEST)
        token  = request.headers['Authorization'][6:]
        return get_veterinarian(token)

class AuthorizedAnimals(APIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        veterinarian = check_authentication(request) 
        list_authorized_animals = Authorization.objects.filter(veterinarian=veterinarian).values_list('animal', flat=True)
        authorized_animals = Animals.objects.filter(id__in=list_authorized_animals)
        serializer = AnimalSerializer(authorized_animals, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)        
    pass