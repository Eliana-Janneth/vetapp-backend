from django.contrib import admin
from veterinarian_information.models import AcademicInformation, WorkExperience

class AcademicInformationAdmin(admin.ModelAdmin):
    list_display = ("veterinarian","title","university","year")


class WorkExperienceAdmin(admin.ModelAdmin):
    list_display = ("veterinarian","title","company","start_date")

admin.site.register(AcademicInformation,AcademicInformationAdmin)
admin.site.register(WorkExperience,WorkExperienceAdmin)

