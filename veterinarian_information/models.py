from django.db import models
from users.models import Veterinarian

class AcademicInformation(models.Model):
    id = models.AutoField(primary_key=True)
    veterinarian = models.ForeignKey(Veterinarian, on_delete=models.CASCADE)
    title = models.CharField(max_length=256)
    university = models.CharField(max_length=100)
    year = models.DateField()
    country = models.CharField(max_length=32)
    academic_degree = models.CharField(max_length=100)
    currently = models.BooleanField(default=False)
    added_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Chat: {self.academic_degree} - {self.title}"
    
    class Meta:
        verbose_name = 'Información académica'
        verbose_name_plural = 'Informaciones académicas'

class WorkExperience(models.Model):
    id = models.AutoField(primary_key=True)
    veterinarian = models.ForeignKey(Veterinarian, on_delete=models.CASCADE)
    title = models.CharField(max_length=256)
    company = models.CharField(max_length=100)
    functions = models.CharField(max_length=256)
    start_date = models.DateField()
    end_date = models.DateField(null=True)
    country = models.CharField(max_length=32)
    currently = models.BooleanField(default=False)
    added_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.company} - {self.start_date}"
    
    class Meta:
        verbose_name = 'Experiencia laboral'
        verbose_name_plural = 'Experiencias laborales'