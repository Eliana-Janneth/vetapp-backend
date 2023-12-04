from helpers.views.auth_vet_view import AuthVetMixin
from animals.models import Animals
from farmer_request.models import Authorization
from animals.serializers.animals import AnimalSerializer
from rest_framework.response import Response
from rest_framework.views import APIView


class AnimalInfoVet(AuthVetMixin, APIView):
    def get(self, request, animal_id):
        try:
            vet = self.check_authentication(request)
            animal = Animals.objects.get(id=animal_id)
            authorization = Authorization.objects.get(
                veterinarian=vet, animal=animal)
            if authorization.animal.id != animal.id and vet.id != authorization.veterinarian.id:
                return self.handle_error_response()
            serializer = AnimalSerializer(animal)
            return Response(serializer.data)
        except (Animals.DoesNotExist, Authorization.DoesNotExist):
            return self.handle_error_response()
