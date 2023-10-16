from django.contrib import admin
from farmer_request.models import FarmerRequest, Authorization
# Register your models here.
class VeterinarianAuthorizationsAdmin(admin.ModelAdmin):
    list_display = ("animal","veterinarian")

admin.site.register(Authorization,VeterinarianAuthorizationsAdmin)