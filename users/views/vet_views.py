from helpers.views.user_view import UserMixin
from helpers.views.auth_vet_view import AuthVetMixin
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import serializers
from users.serializers.veterinarian_serializer import VeterinarianSerializer
from users.models import Veterinarian

class VeterinarianBasic(UserMixin, APIView):

    def post(self, request):
        serializer = VeterinarianSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.check_users_exists(serializer.validated_data)
        self.create_veterinarian(serializer)
        return Response({'response': 'Te has registrado existosamente'}, status=status.HTTP_201_CREATED)

    def create_veterinarian(self, veterinarian_serializer):
        try:
            veterinarian_serializer.save()
        except Exception:
            raise serializers.ValidationError(
                {'response': 'Ha ocurrido un error al registrarte, intentalo nuevamente más tarde'})


class VeterinarianAuthenticated(AuthVetMixin, APIView):

    def get(self, request):
        veterinarian = self.check_authentication(request)
        if not veterinarian:
            return self.handle_error_response()
        veterinarian = Veterinarian.objects.get(id=veterinarian.id)
        serializer = VeterinarianSerializer(veterinarian)
        return Response(serializer.data)

    def patch(self, request, *args, **kwargs):
        
        veterinarian = self.check_authentication(request)
        if not veterinarian:
            return self.handle_error_response()
        serializer = VeterinarianSerializer(
            veterinarian, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)


class VeterinarianAvailabilityUpdateView(AuthVetMixin, APIView):
    def patch(self, request):
        veterinarian = self.check_authentication(request)
        if not veterinarian:
            return self.handle_error_response()
        veterinarian = Veterinarian.objects.get(id=veterinarian.id)
        veterinarian.available = not veterinarian.available
        veterinarian.save()
        serializer = VeterinarianSerializer(veterinarian)
        return Response(serializer.data)