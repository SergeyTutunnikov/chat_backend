from django.shortcuts import render
from rest_framework import generics
from .serializers import *
from .models import *

class SendMessage(generics.CreateAPIView):
    serializer_class=ChatMessageSerializer

class GetMessages(generics.ListAPIView):
    serializer_class=ChatMessageSerializer
    def get_queryset(self):
        sender_id=self.kwargs.get("sender_id")        
        receiver_id=self.kwargs.get("receiver_id")
        return ChatMessage.objects.filter(
            sender__in=[sender_id,receiver_id],
            receiver__in=[sender_id,receiver_id]
        )