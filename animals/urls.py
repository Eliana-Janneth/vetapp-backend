from django.urls import path
from animals import views
from animals.views.animals_view import AnimalsFarmer, AnimalDetail, AnimalSearchByName, AnimalList
from animals.views.animal_species_view import AnimalSpeciesList
from animals.views.animal_races_view import AnimalRaceList, AnimalRaceBySpecie

urlpatterns = [
    path('animals/', AnimalsFarmer.as_view(), name='animals'),
    path('animals-list/', AnimalList.as_view(), name='animals-list'),
    path('animals/<int:pk>/', AnimalDetail.as_view(), name='animal-detail'),
    path('animals/search/', AnimalSearchByName.as_view(), name='animal-search-by-name'),
    path('animal-species/', AnimalSpeciesList.as_view(), name='animal-species-list'),
    path('animal-races/', AnimalRaceList.as_view(), name='animal-race-list'),
    path('animal-specie-races/<int:specie_id>', AnimalRaceBySpecie.as_view(), name='animal-race-list'),
    
]
