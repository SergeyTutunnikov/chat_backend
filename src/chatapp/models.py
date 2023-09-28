from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save

class ChatMessage(models.Model):
    sender=models.ForeignKey(User,on_delete=models.CASCADE,related_name='sender')
    receiver=models.ForeignKey(User,on_delete=models.CASCADE,related_name='receiver')
    user=models.ForeignKey(User,on_delete=models.CASCADE,related_name='user')
    message=models.CharField(max_length=10000)
    is_read=models.BooleanField(default=False)
    date=models.DateTimeField(auto_now_add=True)
    class Meta:
        ordering=['date']
    
    def __str__(self):
        return f'{self.sender} ==> {self.receiver}'

    @property
    def sender_profile(self):
        profile=Profile.objects.get(user=self.sender)
        return profile
        
    @property
    def receiver_profile(self):
        profile=Profile.objects.get(user=self.receiver)
        return profile

class Profile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    status=models.CharField(max_length=100)
    avatar=models.ImageField(upload_to='avatars',default="avatar.jpg")
    verified=models.BooleanField(default=False)

def create_user_profile(sender,instance,created,*args, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    
def save_user_profile(sender,instance,*args,**kwargs):
    instance.profile.save()

post_save.connect(create_user_profile,sender=User)
post_save.connect(save_user_profile,sender=User)