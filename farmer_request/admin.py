from django.contrib import admin
from farmer_request.models import FarmerRequest, Authorization

class VeterinarianAuthorizationsAdmin(admin.ModelAdmin):
    list_display = ("animal","veterinarian")

class FarmerRequestAdmin(admin.ModelAdmin):
    list_display = ("animal","veterinarian")

admin.site.register(FarmerRequest,FarmerRequestAdmin)
admin.site.register(Authorization,VeterinarianAuthorizationsAdmin)