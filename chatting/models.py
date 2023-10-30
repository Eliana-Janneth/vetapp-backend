from django.db import models
from users.models import Farmer, Veterinarian, User
from animals.models import Animals
from django.utils import timezone


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

    def get_farmer_chats_by_animal_name(self, farmer_id, animal_name):
        return Chat.objects.filter(farmer__id=farmer_id, animal__name__icontains=animal_name)

    def get_vet_chats_by_animal_name(self, vet_id, animal_name):
        return Chat.objects.filter(veterinarian__id = vet_id, animal__name__icontains=animal_name)
    
    def get_chats_by_farmer_name(self, vet_id, farmer_name):
        return Chat.objects.filter(veterinarian__id = vet_id, farmer__first_name__icontains=farmer_name)

    def get_chats_by_vet_name(self, farmer_id, vet_name):
        return Chat.objects.filter(farmer__id=farmer_id, veterinarian__first_name__icontains=vet_name)

    def get_chats_by_farmer_and_animal_name(self, vet_id, farmer_name, animal_name):
        return Chat.objects.filter(
            veterinarian__id=vet_id,
            farmer__first_name__icontains=farmer_name,
            animal__name__icontains=animal_name
        )

    def get_chats_by_vet_and_animal_name(self, farmer_id, vet_name, animal_name):
        return Chat.objects.filter(
            farmer__id=farmer_id,
            veterinarian__first_name__icontains=vet_name,
            animal__name__icontains=animal_name
        )

    def __str__(self):
        return f"Chat: {self.farmer} - {self.veterinarian}"

    class Meta:
        verbose_name = 'Chat'
        verbose_name_plural = 'Chats'


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
