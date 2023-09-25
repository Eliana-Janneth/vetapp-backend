from django.urls import path
from animals import views

urlpatterns = [
    path('animal-species/', views.AnimalSpeciesList.as_view(), name='animal-species-list'),
    path('animal-races/', views.AnimalRaceList.as_view(), name='animal-race-list'),
    path('animals/', views.AnimalList.as_view(), name='animal-list'),
]
