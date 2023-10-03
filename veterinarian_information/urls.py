from django.urls import path
from veterinarian_information import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = format_suffix_patterns([
    path('vet-academic-information/', views.AcademicInformationVet.as_view()),
    path('vet-work-experience/', views.WorkExperienceVet.as_view())
])