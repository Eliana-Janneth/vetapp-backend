from django.contrib import admin
from medical_history.models import MedicalHistory

# Register your models here.
class VeterinarianConsultationsAdmin(admin.ModelAdmin):
    list_display = ("id","animal","veterinarian","create_date","diagnosis","treatment")

admin.site.register(MedicalHistory,VeterinarianConsultationsAdmin)