from django.urls import path
from animals import views

urlpatterns = [
    path('animals/', views.AnimalList.as_view(), name='animals-list'),
    path('animals/<int:id>/', views.AnimalDetail.as_view(), name='animals-detail'),
    path('animals/species/', views.AnimalSpeciesList.as_view()),
    path('animals/species/<int:id>/', views.AnimalSpeciesDetail.as_view()),
    path('animals/species/races/', views.AnimalRaceList.as_view()),
    path('animals/species/races/<int:id>', views.AnimalRaceDetail.as_view()),

]
