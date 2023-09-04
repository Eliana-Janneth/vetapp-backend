from django.db import models

# Create your models here.
class Veterinary_Consultations(models.Model):
    id = models.AutoField(primary_key=True)
    veterinarian = models.CharField(max_length=100) #TODO: change to foreign key
    animal = models.CharField(max_length=100) #TODO: change to foreign key
    date = models.DateField()
    diagnostic = models.CharField(max_length=1000)
    treatment = models.CharField(max_length=1000)
    