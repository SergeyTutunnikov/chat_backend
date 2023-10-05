from django.shortcuts import render
from rest_framework import generics
from .serializers import *
from .models import *
from django.db.models import Subquery,OuterRef,Q
from django.contrib.auth.models import User



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
class GetInBox(generics.ListAPIView):
    serializer_class=ChatMessageSerializer
    def get_queryset(self):
        user_id=self.kwargs.get('user_id')
        messages=ChatMessage.objects.filter(
            id__in=Subquery(
                User.objects.filter(
                    Q(sender__receiver=user_id)|Q(receiver__sender=user_id)
                )
                .distinct()
                .annotate(
                    last_msg=Subquery(
                        ChatMessage.objects.filter(
                            Q(sender=OuterRef('id'),receiver=user_id)|Q(receiver=OuterRef('id'),sender=user_id)
                        ).order_by('-id')[:1].values_list('id',flat=True)
                    )
                ).values_list('last_msg',flat=True).order_by('-id')
            )

        ).order_by('-id')
        print(messages)
        return messages
        