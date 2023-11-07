from helpers.views.auth_farmer_view import AuthFarmerMixin
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from animals.models import Animals, AnimalRaces, AnimalSpecies
from animals.serializers.animals import AnimalSerializer, AnimalListSerializer, AnimalUpdateSerializer
from django.db.models import Q

class AnimalsFarmer(AuthFarmerMixin, APIView):

    def get(self, request):
        farmer = self.check_authentication(request)
        if not farmer:
            return self.handle_error_response()
        animals = Animals.objects.filter(farmer=farmer.id)
        animal_serializer = AnimalSerializer(animals, many=True)
        return Response(animal_serializer.data)

    def post(self, request):
        farmer = self.check_authentication(request)
        if not farmer:
            return self.handle_error_response()
        request.data['farmer'] = farmer.id
        serializer = AnimalSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class AnimalDetail(AuthFarmerMixin,APIView):

    def get(self, request, pk):
        farmer = self.check_authentication(request)
        if pk is None:
            return Response({'response': 'El ID del animal es requerido'}, status=status.HTTP_400_BAD_REQUEST)
        try:
            animal = Animals.objects.get(id=pk)
            if animal.farmer.id != farmer.id:
                return self.handle_error_response()
            serializer = AnimalSerializer(animal)
            return Response(serializer.data)
        except Animals.DoesNotExist:    
            return self.handle_error_response()

    def patch(self, request, pk):
        farmer = self.check_authentication(request)
        if pk is None:
            return Response({'response': 'El ID del animal es requerido'}, status=status.HTTP_400_BAD_REQUEST)
        try:
            animal = Animals.objects.get(id=pk)
            if animal.farmer.id != farmer.id:
                return self.handle_error_response()
            serializer = AnimalUpdateSerializer(animal, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                updated_animal = Animals.objects.get(id=pk)
                updated_serializer = AnimalSerializer(updated_animal)
                return Response(updated_serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Animals.DoesNotExist:
            return self.handle_error_response()


class AnimalSearchByName(AuthFarmerMixin, APIView):
    def get(self, request):
        farmer = self.check_authentication(request)
        try:
            if not farmer:
                return self.handle_error_response()
            search_query = request.query_params.get('by', '')
            if search_query == '':
                return Response({'response': 'El nombre del animal es requerido'}, status=status.HTTP_400_BAD_REQUEST)
            animals = Animals.objects.filter(farmer=farmer.id)
            animals = animals.filter(Q(name__icontains=search_query)|Q(race__in=AnimalRaces.objects.filter(Q(name__icontains=search_query))) |
                                             Q(specie__in=AnimalSpecies.objects.filter(Q(name__icontains=search_query))))
            serializer = AnimalSerializer(animals, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Animals.DoesNotExist:
            return Response({'response': 'No se encontraron animales con el nombre especificado'}, status=status.HTTP_404_NOT_FOUND)

class AnimalList(AuthFarmerMixin,APIView):
    def get(self, request):
        farmer = self.check_authentication(request)
        if not farmer:
            return self.handle_error_response()
        try:
            animals = Animals.objects.filter(farmer=farmer.id)
            animal_serializer = AnimalListSerializer(animals, many=True)
            return Response(animal_serializer.data)
        except Animals.DoesNotExist:
            return Response({'response': 'No se encontraron animales'}, status=status.HTTP_404_NOT_FOUND)