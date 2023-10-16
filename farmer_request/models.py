from django.db import models
from users.models import Farmer, Veterinarian
from animals.models import Animals


class FarmerRequest(models.Model):
    id = models.AutoField(primary_key=True)
    farmer = models.ForeignKey(Farmer, on_delete=models.CASCADE)
    veterinarian = models.ForeignKey(Veterinarian, on_delete=models.CASCADE)
    Animal = models.ForeignKey(Animals, on_delete=models.CASCADE)
    message = models.TextField(max_length=512)

    def __str__(self):
        return f"{self.farmer} - {self.animal}"    
    
    class Meta:
        verbose_name = 'Solicitud de veterinario'
        verbose_name_plural = 'Solcitudes de veterinarios'

class Authorization(models.Model):
    id = models.AutoField(primary_key=True)
    animal = models.ForeignKey(Animals, on_delete=models.CASCADE)
    veterinarian = models.ForeignKey(Veterinarian, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    state = models.BooleanField(default=False)
    update_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.animal} - {self.veterinarian}"    
    
    class Meta:
        verbose_name = 'Autorización'
        verbose_name_plural = 'Autorizaciones'