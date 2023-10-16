from django.contrib import admin
from animals.models import Animals, AnimalSpecies, AnimalRaces

class AnimalAdmin(admin.ModelAdmin):
    list_display = ("id","name","specie","weight")

class AnimalSpecieAdmin(admin.ModelAdmin):
    list_display = ("id","name",)

class AnimalRaceAdmin(admin.ModelAdmin):
    list_display = ("id","name",)

admin.site.register(Animals,AnimalAdmin)
admin.site.register(AnimalSpecies,AnimalSpecieAdmin)
admin.site.register(AnimalRaces,AnimalRaceAdmin)