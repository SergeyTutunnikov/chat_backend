from django.contrib import admin
from .models import *

class ChatMessageAdmin(admin.ModelAdmin):
    list_display=["sender","receiver","message","is_read","date"]
    list_editable=["is_read"]

admin.site.register(ChatMessage,ChatMessageAdmin)
admin.site.register(Profile)
