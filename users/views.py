from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from users.models import Farmer, Veterinarian
from users.serializers import FarmerSerializer, VeterinarianSerializer

# Create your views here.
class FarmerList(APIView):

    def get(self, request):
        farmers_list = Farmer.objects.all()
        serializer = FarmerSerializer(farmers_list, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = FarmerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(request.data, status=status.HTTP_400_BAD_REQUEST)

class FarmerDetail(APIView):

    def get_object(self, id):
        pass

    def get(self, request, id):
        pass

    def put(self, request, id):
        pass

    def delete(self, request, id):
        pass


class FarmerList(APIView):

    def get(self, request):
        farmers_list = Farmer.objects.all()
        serializer = VeterinarianSerializer(farmers_list, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = VeterinarianSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(request.data, status=status.HTTP_400_BAD_REQUEST)
    
class VeterinarianDetail(APIView):

    def get_object(self, id):
        pass

    def get(self, request, id):
        pass

    def put(self, request, id):
        pass

    def delete(self, request, id):
        pass