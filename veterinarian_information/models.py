from django.db import models

# Create your models here.
class Academic_Information(models.Model):
    id = models.AutoField(primary_key=True)
    veterinarian = models.CharField(max_length=100) #TODO: change to foreign key
    title = models.CharField(max_length=256)
    university = models.CharField(max_length=100)
    year = models.IntegerField()
    country = models.CharField(max_length=32)
    academic_degree = models.CharField(max_length=100)
    currently_studying = models.BooleanField()
    duration = models.IntegerField()
    added_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Chat: {self.academic_degree} - {self.title}"
    
    class Meta:
        verbose_name = 'Información académica'
        verbose_name_plural = 'Informaciones académicas'

class Work_Experience(models.Model):
    id = models.AutoField(primary_key=True)
    veterinarian = models.CharField(max_length=100) #TODO: change to foreign key
    title = models.CharField(max_length=256)
    company = models.CharField(max_length=100)
    functions = models.CharField(max_length=256)
    start_date = models.IntegerField()
    end_date = models.IntegerField(null=True)
    country = models.CharField(max_length=32)
    currently_working = models.BooleanField()
    duration = models.IntegerField()
    added_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.company} - {self.last_name}"
    
    class Meta:
        verbose_name = 'Experiencia laboral'
        verbose_name_plural = 'Experiencias laborales'