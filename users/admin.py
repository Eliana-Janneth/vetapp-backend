from django.contrib import admin
from users.models import Farmer,Veterinarian


class FarmerAdmin(admin.ModelAdmin):
    list_display = ("id","first_name","last_name","email","phone_number","address","city","password")

class VeterinarianAdmin(admin.ModelAdmin):
    list_display = ("id","first_name","last_name","email","phone_number","address","city")

admin.site.register(Farmer,FarmerAdmin)
admin.site.register(Veterinarian,VeterinarianAdmin)
