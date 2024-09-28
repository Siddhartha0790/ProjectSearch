from django.db import models
from django.contrib.auth.models import User
#from django.contrib.auth.models import 
from django.db.models import signals
from .models import Profile
from django.core.mail import send_mail
from django.conf import settings


def sendsignal(sender , instance ,created ,**kwargs):
    print('Profile updated', created , instance)
    
def createprofile(sender, created,instance,**kwargs):
    
    if created:
        user = instance
        Profile.objects.create(
        user=user,
        username = user.username,
        name = user.first_name ,  
        email= user.email      
        )
        print('created new user')
        send_mail(
        "Thanks for joining devsearch",
        "dive into the world of crazy projects.",
        settings.EMAIL_HOST_USER,
        [user.profile.email],
        fail_silently=False,
)
          
def deleteprofile(sender, instance , **kwargs):
    user = instance.user
    user.delete()
    
def updateprofile(sender,instance,created , **kwargs):
    pass
    profile = instance
    if not created:
        profile.user.email = profile.email
        profile.user.first_name = profile.name

signals.post_save.connect(sendsignal, sender=Profile)

signals.post_save.connect(createprofile, sender=User)

signals.post_delete.connect(deleteprofile , sender= Profile)

signals.post_save.connect(updateprofile , sender = Profile)