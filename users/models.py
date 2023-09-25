from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=40)
    document_number = models.CharField(max_length=20, unique=True) 
    email = models.EmailField(unique = True)
    password = models.CharField(max_length=200)
    phone_number = models.CharField(max_length=15)
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=50)
    role = models.CharField(max_length=20)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'password']
    
    def save(self, *args, **kwargs):
        if not self.pk:
            return super().save(*args, **kwargs)

    class Meta:
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'

class Farmer(User):

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    class Meta:
        verbose_name = 'Granjero'
        verbose_name_plural = 'Granjeros'

class Veterinarian(User):
    licence_number = models.CharField(max_length=20, null = True, blank = True)
    license_expiry_date = models.DateField(null=True, blank=True)
    

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    class Meta:
        verbose_name = 'Veterinario'
        verbose_name_plural = 'Veterinarios'