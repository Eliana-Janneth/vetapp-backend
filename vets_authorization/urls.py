from django.urls import path
from vets_authorization.views.authorization_view import AuthorizedAnimals
from vets_authorization.views.create_vet_auth_view import Authorization
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = format_suffix_patterns([
    path('authorized-animals/', AuthorizedAnimals.as_view()),
    path('authorization/', Authorization.as_view())
])
