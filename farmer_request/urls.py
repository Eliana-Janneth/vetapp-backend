from django.urls import path
from farmer_request.views.authorization_view import AuthorizedAnimals
from farmer_request.views.create_vet_auth_view import Authorization
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = format_suffix_patterns([
    path('authorized-animals/', AuthorizedAnimals.as_view()),
    path('authorization/', Authorization.as_view())
])
