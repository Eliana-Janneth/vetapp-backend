from django.db import models

# Create your models here.
class Academic_Information(models.Model):
    id = models.AutoField(primary_key=True)
    veterinarian = models.CharField(max_length=100) #TODO: change to foreign key
    title = models.CharField(max_length=100)
    university = models.CharField(max_length=100)
    year = models.IntegerField()
    country = models.CharField(max_length=100)
    academic_degree = models.CharField(max_length=100)
    currently_studying = models.BooleanField()
    duration = models.IntegerField()

class Work_Experience(models.Model):
    id = models.AutoField(primary_key=True)
    veterinarian = models.CharField(max_length=100) #TODO: change to foreign key
    title = models.CharField(max_length=100)
    company = models.CharField(max_length=100)
    functions = models.CharField(max_length=100)
    start_date = models.IntegerField()
    end_date = models.IntegerField()
    country = models.CharField(max_length=100)
    currently_working = models.BooleanField()
    duration = models.IntegerField()