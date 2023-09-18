from django.db import models
from animals.models import Animals
from users.models import Veterinarian

class Veterinary_Consultations(models.Model):
    id = models.AutoField(primary_key=True)
    veterinarian = models.ForeignKey(Veterinarian, on_delete=models.CASCADE) 
    animal = models.ForeignKey(Animals, on_delete=models.CASCADE)
    create_date = models.DateField(auto_now_add=True)
    diagnostic = models.CharField(max_length=2048)
    treatment = models.CharField(max_length=2048)

    def __str__(self):
        return f"{self.veterinarian} - {self.create_date}"
    
    class Meta:
        verbose_name = 'Consulta veterinaria'
        verbose_name_plural = 'Consultas veterinarias'
    