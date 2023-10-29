from django.contrib import admin
from chatting.models import Chat, Message

class ChatAdmin(admin.ModelAdmin):
    list_display = ("id",)

admin.site.register(Chat, ChatAdmin)

class MesssageAdmin(admin.ModelAdmin):
    list_display = ("id","chat","sender","message","date_sent")

admin.site.register(Message, MesssageAdmin)