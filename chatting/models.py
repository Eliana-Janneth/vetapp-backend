from django.db import models

# Create your models here.
class Message(models.Model):
    id = models.AutoField(primary_key=True)
    chat = models.CharField(max_length=100) #TODO: change to foreign key
    sender = models.CharField(max_length=100) #TODO: change to foreign key
    receiver = models.CharField(max_length=100) #TODO: change to foreign key
    message = models.CharField(max_length=1000)
    date_sent = models.DateTimeField(auto_now_add=True)
    images = models.ImageField(upload_to='images/', blank=True)
    videos = models.FileField(upload_to='videos/', blank=True)
    documents = models.FileField(upload_to='documents/' , blank=True)


class Chat(models.Model):
    id = models.AutoField(primary_key=True)
    farmer = models.CharField(max_length=100) #TODO: change to foreign key
    veterinarian = models.CharField(max_length=100) #TODO: change to foreign key
    
