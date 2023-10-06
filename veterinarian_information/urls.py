from django.urls import path
from veterinarian_information.views.academic_info_view import AcademicInformationVet
from veterinarian_information.views.work_experience_view import WorkExperienceVet
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = format_suffix_patterns([
    path('vet-academic-information/', AcademicInformationVet.as_view()),
    path('vet-work-experience/', WorkExperienceVet.as_view())
])