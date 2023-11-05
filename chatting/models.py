from django.db import models
from users.models import Farmer, Veterinarian, User
from animals.models import Animals
from django.utils import timezone
from django.db.models import Q

class Chat(models.Model):
    id = models.AutoField(primary_key=True)
    farmer = models.ForeignKey(Farmer, on_delete=models.CASCADE)
    veterinarian = models.ForeignKey(Veterinarian, on_delete=models.CASCADE)
    animal = models.ForeignKey(Animals, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(default=timezone.now)

    def update_modified(self):
        self.modified = timezone.now()
        self.save()

    @staticmethod
    def get_chats_by_farmer_or_animal_name(vet_id, name):
        return Chat.objects.filter(
            Q(veterinarian__id=vet_id),
            Q(animal__name__icontains=name) | Q(farmer__first_name__icontains=name) | Q(farmer__last_name__icontains=name)
        )

    @staticmethod
    def get_chats_by_vet_or_animal_name(farmer_id, name):
        return Chat.objects.filter(
            Q(farmer__id=farmer_id),
            Q(animal__name__icontains=name) | Q(veterinarian__first_name__icontains=name) | Q(veterinarian__last_name__icontains=name)
        )
    def __str__(self):
        return f"Chat: {self.farmer} - {self.veterinarian}"

    class Meta:
        verbose_name = 'Chat'
        verbose_name_plural = 'Chats'
        ordering = ('-modified',)


class Message(models.Model):
    id = models.AutoField(primary_key=True)
    chat = models.ForeignKey(Chat, on_delete=models.CASCADE)
    sender = models.ForeignKey(
        User, max_length=15, on_delete=models.SET_NULL, null=True)
    message = models.CharField(max_length=1024)
    date_sent = models.DateTimeField(auto_now_add=True)
    file = models.ImageField(upload_to='chat_files/', blank=True, null=True)

    def save(self, *args, **kwargs):
        self.chat.update_modified()
        super(Message, self).save(*args, **kwargs)

    def __str__(self):
        return f"{self.date_sent} - {self.sender} - {self.message}"

    class Meta:
        verbose_name = 'Mensaje'
        verbose_name_plural = 'Mensajes'
        ordering = ('-date_sent',)
