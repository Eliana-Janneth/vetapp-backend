from django.db import models

# Create your models here.

class Animals(models.Model):
    id = models.AutoField(primary_key=True) 
    name = models.CharField(max_length=100)
    species = models.CharField(max_length=100)
    race = models.CharField(max_length=100)
    color = models.CharField(max_length=100)
    birth_date = models.DateField()
    gender = models.CharField(max_length=100) 
    owner = models.CharField(max_length=100) # TODO: change to foreign key