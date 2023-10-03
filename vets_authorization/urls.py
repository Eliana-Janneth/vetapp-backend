from django.urls import path
from vets_authorization import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = format_suffix_patterns([
    path('authorized-animals/', views.AuthorizedAnimals.as_view()),
])
