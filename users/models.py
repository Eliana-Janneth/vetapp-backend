from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.mail import send_mail
import environ
env = environ.Env()


class User(AbstractUser):
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=40)
    document_number = models.CharField(max_length=20, unique=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=200)
    phone_number = models.CharField(max_length=15)
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=50)
    role = models.CharField(max_length=20)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'password']

    class Meta:
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'

    def notify_message(self, farmer_request):
        pass


class Farmer(User):

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    class Meta:
        verbose_name = 'Granjero'
        verbose_name_plural = 'Granjeros'

    def notify_message(self, farmer_request):
        subject = f"Vetapp - Respuesta a solicitud de veterinario para {farmer_request.animal}"

        if farmer_request.status == 1:
            response = f"""
            {farmer_request.veterinarian} ha aceptado su solicitud para atender a {farmer_request.animal}.
            Ahora puedes ingresar a nuestra plataforma y empezar a chatear para mejorar la salud del animal.\n
            """
        if farmer_request.status == 2:
            response = f"""
            {farmer_request.veterinarian} ha rechazado su solicitud para atender a {farmer_request.animal}. Te recomendamos buscar un nuevo veterinario.\n
                        """

        message = f"""
        Estimado Granjero,\n\n
        Ha recibido una respuesta a su solicitud para atender a {farmer_request.animal} por parte de {farmer_request.veterinarian}.\n\n
        {response}
        \n\nAtentamente,
        \nEl Equipo de tu aplicación
        """
        send_mail(
            subject,
            message,
            env('EMAIL_HOST_USER'),
            [self.email],
            fail_silently=False,
        )


class Veterinarian(User):
    license_number = models.CharField(max_length=20, null=True, blank=True)
    license_expiry_date = models.DateField(null=True, blank=True)
    available = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    class Meta:
        verbose_name = 'Veterinario'
        verbose_name_plural = 'Veterinarios'

    # Reemplaza 'from@example.com' con tu dirección de correo electrónico
    def notify_message(self, farmer_request):
        subject = f"Vetapp - Solicitud de veterinario para {farmer_request.animal} por {farmer_request.farmer}"
        message = f"""Estimado Veterinario,\n\n
        Se ha realizado una solicitud para atender a {farmer_request.animal} por parte de {farmer_request.farmer}.
        \n\nMensaje: {farmer_request.message}
        \n\nAtentamente,
        \nEl Equipo de Vetapp"""
        send_mail(
            subject,
            message,
            env('EMAIL_HOST_USER'),
            [self.email],
            fail_silently=False,
        )
