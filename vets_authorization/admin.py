from django.contrib import admin
from vets_authorization.models import Authorization

# Register your models here.
class VeterinarianAuthorizationsAdmin(admin.ModelAdmin):
    list_display = ("animal","veterinarian")

admin.site.register(Authorization,VeterinarianAuthorizationsAdmin)