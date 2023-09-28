from .models import *
from rest_framework import serializers
class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model=Profile
        fields=['id','user','status','avatar','verified']

class ChatMessageSerializer(serializers.ModelSerializer):
    sender_profile=ProfileSerializer(read_only=True)
    receiver_profile=ProfileSerializer(read_only=True)
    class Meta:
        model=ChatMessage
        fields=['user','sender','receiver','sender_profile','receiver_profile','message','is_read','date','id']