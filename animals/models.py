from django.db import models
from users.models import Farmer


class Animal_Species(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name = 'Especie de animal'
        verbose_name_plural = 'Especies de animales'


class Animal_Race(models.Model):
    id = models.AutoField(primary_key=True)
    specie = models.ForeignKey(Animal_Species, on_delete=models.CASCADE)
    name = models.CharField(max_length=45)

    def __str__(self):
        return f"{self.name} - {self.specie}"

    class Meta:
        verbose_name = 'Raza de animal'
        verbose_name_plural = 'Razas de animales'


class Animals(models.Model):
    id = models.AutoField(primary_key=True)
    farmer = models.ForeignKey(Farmer, on_delete=models.CASCADE)
    name = models.CharField(max_length=45)
    specie = models.ForeignKey(Animal_Species, on_delete=models.CASCADE)
    race = models.ForeignKey(Animal_Race, on_delete=models.CASCADE)
    color = models.CharField(max_length=200)
    birth_date = models.DateField()
    gender = models.CharField(max_length=10)
    weight = models.CharField(max_length=10, blank=True, null=True)
    height = models.CharField(max_length=10, blank=True, null=True)
    description = models.CharField(max_length=1000, blank=True, null=True)
    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)

    def get_absolute_url(self):
        return self.post.get_absolute_url()

    def __str__(self):
        return f"{self.specie} - {self.name}"

    class Meta:
        verbose_name = 'Animal'
        verbose_name_plural = 'Animales'