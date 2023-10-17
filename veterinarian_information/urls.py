from django.urls import path
from veterinarian_information.views.academic_info_view import AcademicInformationVet, AcademicInformationVetList
from veterinarian_information.views.work_experience_view import WorkExperienceVet, WorkExperienceVetList
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = format_suffix_patterns([
    path('vet-academic-information/', AcademicInformationVet.as_view()),
    path('vet-academic-information/<int:vet_id>/', AcademicInformationVetList.as_view(), name='vet-academic-info-list'),
    path('vet-work-experience/', WorkExperienceVet.as_view()),
    path('vet-work_experience/<int:vet_id>/', WorkExperienceVetList.as_view(), name='vet-work-experience-list'),
])