from django.db import models

# Create your models here.
class Authorization(models.Model):
    id = models.AutoField(primary_key=True)
    animal = models.CharField(max_length=100) #TODO: change to foreign key
    veterinarian = models.CharField(max_length=100) #TODO: change to foreign key
    date = models.DateField()
    