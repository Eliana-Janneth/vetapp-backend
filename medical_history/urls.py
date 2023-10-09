from django.urls import path
from medical_history.views.animal_medical_history_view import VetMedicalHistory, FarmerMedicalHistory
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = format_suffix_patterns([
    path('vet-medical-historys/<int:animal_id>', VetMedicalHistory.as_view()),
    path('farmer-medical-historys/<int:animal_id>', FarmerMedicalHistory.as_view()),
])