from django.contrib import admin
from medical_history.models import Veterinary_Consultations

# Register your models here.
class VeterinarianConsultationsAdmin(admin.ModelAdmin):
    list_display = ("id","animal","veterinarian","create_date","diagnosis","treatment")

admin.site.register(Veterinary_Consultations,VeterinarianConsultationsAdmin)