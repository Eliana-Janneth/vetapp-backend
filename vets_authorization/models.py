from django.db import models
from animals.models import Animals
from users.models import Veterinarian
# Create your models here.

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