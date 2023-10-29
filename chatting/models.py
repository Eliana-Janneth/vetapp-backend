from django.db import models
from users.models import Farmer, Veterinarian, User
from animals.models import Animals

class Chat(models.Model):
    id = models.AutoField(primary_key=True)
    farmer = models.ForeignKey(Farmer, on_delete=models.CASCADE)
    veterinarian = models.ForeignKey(Veterinarian, on_delete=models.CASCADE)
    animal = models.ForeignKey(Animals, on_delete=models.CASCADE)
    start_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Chat: {self.farmer} - {self.veterinarian}"

    class Meta:
        verbose_name = 'Chat'
        verbose_name_plural = 'Chats'

class Message(models.Model):
    id = models.AutoField(primary_key=True)
    chat = models.ForeignKey(Chat,on_delete=models.CASCADE)
    sender = models.ForeignKey(User, max_length=15, on_delete=models.SET_NULL, null=True)
    message = models.CharField(max_length=1024)
    date_sent = models.DateTimeField(auto_now_add=True)
    file = models.ImageField(upload_to='chat_files/', blank=True, null=True)

    def __str__(self):
        return f"{self.date_sent} - {self.sender} - {self.message}"

    class Meta:
        verbose_name = 'Mensaje'
        verbose_name_plural = 'Mensajes'
        ordering = ('-date_sent',)

