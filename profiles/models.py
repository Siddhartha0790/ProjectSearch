from django.db import models
from django.contrib.auth.models import User
#from django.contrib.auth.models import 
from django.db.models import signals

class Skills(models.Model):
  
    name = models.CharField(max_length=50,null=True,blank=True)
    description= models.TextField(max_length=500,null=True,blank=True)
    def __str__(self):
        return self.name

class Profile(models.Model):
    user= models.OneToOneField(User, on_delete=models.CASCADE)
    username = models.CharField(max_length=50,null=True,blank=True)
    location = models.CharField(max_length=100, default='Earth')
    name= models.CharField(max_length=100)
    Profile_pic = models.ImageField(blank=True,null=True,default= '/images/profilepic.webp' )
    shortbio = models.CharField(max_length=100, null=True,blank=True)
    bio = models.TextField(blank=True,null=True,max_length=500)
    email= models.EmailField(blank=True,null=True,max_length=500)
    social_github = models.CharField(blank=True,null=True,max_length=300)
    social_twitter = models.CharField(blank=True,null=True,max_length=300)
    social_linkedin = models.CharField(blank=True,null=True,max_length=300)
    social_reddit = models.CharField(blank=True,null=True,max_length=300)
    created = models.DateTimeField(auto_now_add=True,null=True)
    skills = models.ManyToManyField(Skills)
    
    def __str__(self):
        return str(self.user.username)
# Create your models here.

class Inbox(models.Model):
    owner = models.ForeignKey(Profile, on_delete=models.PROTECT)
    receiver = models.ForeignKey(Profile, on_delete= models.CASCADE, related_name='messages')
    content = models.TextField(max_length=200,null=True, blank=True)
    