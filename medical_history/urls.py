from django.urls import path
from medical_history.views.animal_medical_history_view import VetMedicalHistory, FarmerMedicalHistory
from medical_history.views.vet_get_animal_info import AnimalInfoVet
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = format_suffix_patterns([
    path('vet-medical-historys/<int:animal_id>/', VetMedicalHistory.as_view()),
    path('vet-medical-historys/<int:animal_id>/<int:medical_history_id>/', VetMedicalHistory.as_view(), name='vet-medical-history-detail'),
    path('farmer-medical-historys/<int:animal_id>/', FarmerMedicalHistory.as_view()),
    path('vet-animal-info/<int:animal_id>/', AnimalInfoVet.as_view()),
])