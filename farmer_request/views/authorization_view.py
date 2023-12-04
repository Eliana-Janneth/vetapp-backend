from helpers.views.auth_vet_view import AuthVetMixin
from rest_framework.response import Response
from rest_framework import status
from animals.models import AnimalRaces, AnimalSpecies, Animals
from rest_framework.views import APIView
from farmer_request.models import Authorization
from animals.serializers.animals import AnimalSerializer
from django.db.models import Q

from users.models import Farmer

class AuthorizedAnimals(AuthVetMixin, APIView):

    def get(self, request):
        veterinarian = self.check_authentication(request) 
        if not veterinarian:
            return Response({"error": "Unauthorized"}, status=status.HTTP_401_UNAUTHORIZED)
        list_authorized_animals = Authorization.objects.filter(veterinarian=veterinarian).values_list('animal', flat=True)
        authorized_animals = Animals.objects.filter(id__in=list_authorized_animals).order_by('-authorization__update_time')
        serializer = AnimalSerializer(authorized_animals, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class SearchAuthorizedAnimals(AuthVetMixin, APIView):
    def get(self, request):
        veterinarian = self.check_authentication(request)
        if not veterinarian:
            return Response({"error": "Unauthorized"}, status=status.HTTP_401_UNAUTHORIZED)
        list_authorized_animals = Authorization.objects.filter(veterinarian=veterinarian).values_list('animal', flat=True)
        search_query = request.GET.get('by', None)  
        authorized_animals = Animals.objects.filter(id__in=list_authorized_animals)
        if search_query:
            authorized_animals = authorized_animals.filter(
                Q(name__icontains=search_query) |
                Q(race__in=AnimalRaces.objects.filter(Q(name__icontains=search_query))) |
                Q(specie__in=AnimalSpecies.objects.filter(Q(name__icontains=search_query))) |
                Q(farmer__in=Farmer.objects.filter(Q(first_name__icontains=search_query) | Q(last_name__icontains=search_query)))
            )
        authorized_animals = authorized_animals.order_by('-authorization__update_time')
        serializer = AnimalSerializer(authorized_animals, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)