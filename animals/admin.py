from django.contrib import admin
from animals.models import Animals, Animal_Species, Animal_Race

class AnimalAdmin(admin.ModelAdmin):
    list_display = ("id","name","specie","weight")

class AnimalSpecieAdmin(admin.ModelAdmin):
    list_display = ("id","name",)

class AnimalRaceAdmin(admin.ModelAdmin):
    list_display = ("id","name",)

admin.site.register(Animals,AnimalAdmin)
admin.site.register(Animal_Species,AnimalSpecieAdmin)
admin.site.register(Animal_Race,AnimalRaceAdmin)