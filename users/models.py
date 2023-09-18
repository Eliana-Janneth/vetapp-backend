from django.db import models
from django.contrib.auth.models import AbstractBaseUser

# Create your models here.
class Role(models.TextChoices):
    FARMER = "FARMER", 'Farmer'
    VETERINARIAN = "VETERINARIAN", 'Veterinarian'
    NONE = "NONE", 'None'

class User(AbstractBaseUser):
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=40)
    email = models.EmailField(unique = True)
    password = models.CharField(max_length=30)
    phone_number = models.CharField(max_length=15)
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=50)
    role = Role.NONE
    class Meta:
        abstract = True
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'

class Farmer(User):
    role = Role.FARMER
    ubication = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.first_name} - {self.last_name}"
    class Meta:
        verbose_name = 'Granjero'
        verbose_name_plural = 'Granjeros'

class Veterinarian(User):
    licence_number = models.CharField(max_length=20)
    license_expiry_date = models.DateField()
    role = Role.VETERINARIAN

    def __str__(self):
        return f"{self.first_name} - {self.last_name}"

    class Meta:
        verbose_name = 'Veterinario'
        verbose_name_plural = 'Veterinarios'