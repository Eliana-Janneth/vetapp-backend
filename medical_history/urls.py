from django.urls import path
from medical_history import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = format_suffix_patterns([
    path('vet-consultations/', views.VeterinaryConsultationsAPI.as_view()),
])