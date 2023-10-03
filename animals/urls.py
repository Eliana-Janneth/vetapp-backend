from django.urls import path
from animals import views

urlpatterns = [
    path('animal-species/', views.AnimalSpeciesList.as_view(), name='animal-species-list'),
    path('animal-races/', views.AnimalRaceList.as_view(), name='animal-race-list'),
    path('animal-specie-races/<int:specie_id>', views.AnimalRaceBySpecie.as_view(), name='animal-race-list'),
    path('animals/', views.AnimalFarmer.as_view(), name='animal-list'),
    path('animals/<int:pk>/', views.AnimalDetail.as_view(), name='animal-detail'),
]
