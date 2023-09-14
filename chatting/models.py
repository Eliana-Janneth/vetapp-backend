from django.db import models
from users.models import Farmer, Veterinarian

class Chat(models.Model):
    id = models.AutoField(primary_key=True)
    farmer = models.ForeignKey(Farmer, on_delete=models.CASCADE)
    veterinarian = models.ForeignKey(Veterinarian, on_delete=models.CASCADE)

    def __str__(self):
        return f"Chat: {self.farmer} - {self.veterinarian}"

    class Meta:
        verbose_name = 'Chat'
        verbose_name_plural = 'Chats'

class Message(models.Model):
    id = models.AutoField(primary_key=True)
    chat = models.ForeignKey(Chat,on_delete=models.CASCADE)
    sender = models.CharField(max_length=15) #TODO: Cambiar longitud, poner la del id de veterinario y granjero
    message = models.CharField(max_length=1024)
    date_sent = models.DateTimeField(auto_now_add=True)
    images = models.ImageField(upload_to='images/', blank=True, null=True)
    videos = models.FileField(upload_to='videos/', blank=True, null=True)
    documents = models.FileField(upload_to='documents/' , blank=True, null=True)

    def __str__(self):
        return f"{self.date_sent} - {self.sender} - {self.message}"

    class Meta:
        verbose_name = 'Mensaje'
        verbose_name_plural = 'Mensajes'

