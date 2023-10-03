from django.contrib import admin
from veterinarian_information.models import Academic_Information, Work_Experience

class AcademicInformationAdmin(admin.ModelAdmin):
    list_display = ("veterinarian","title","university","year")


class WorkExperienceAdmin(admin.ModelAdmin):
    list_display = ("veterinarian","title","company","start_date")

admin.site.register(Academic_Information,AcademicInformationAdmin)
admin.site.register(Work_Experience,WorkExperienceAdmin)

