from helpers.views.auth_user_info_view import AuthUserMixin
from rest_framework import status
from chatting.models import Message
from rest_framework.response import Response
from rest_framework.views import APIView
from django.http import FileResponse

class ImageMessageView(AuthUserMixin, APIView):
    def get(self, request, message_id):
        try:
            user = self.get_user_info(request)
            if not user:
                return self.handle_error_response()
            message = Message.objects.get(id=message_id)
            chat = message.chat
            if chat.farmer.id != user.id and chat.veterinarian.id != user.id:
                return self.handle_error_response()
            if not message.file:
                return Response({'response': 'No hay imagen'}, status=status.HTTP_404_NOT_FOUND)
            return FileResponse(message.file)
        except Message.DoesNotExist:
            return self.handle_error_response()