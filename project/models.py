from django.db import models
from profiles.models import Profile
# Create your models here.
from django.db import models
import uuid
# Create your models here.
class Project(models.Model):
    owner = models.ForeignKey(Profile , on_delete= models.CASCADE,null=True,blank=True)
    name = models.CharField(max_length=200,blank=False,null=False)
    description = models.TextField(blank=True,null=True,max_length=500)
    image = models.ImageField(blank=True,null=True,default="ape1.jpg")
    link = models.CharField(blank=True,null=True,max_length=500)
    votes = models.IntegerField(default=0 , blank=True, null = True)
    voteratio = models.IntegerField(default=50, blank=True, null = True)
    tag = models.ManyToManyField('Tag',blank=True)
    created = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['created']
    
    @property
    def votecount(self):
        votes = self.reviews_set.all()
        upvotes = votes.filter(value='up').count()
        totalvotes = votes.count()
        self.votes = upvotes
        self.voteratio = int(upvotes/totalvotes) * 100
        self.save()
    
    def __str__(self):
        return self.name
    
class Reviews(models.Model):
    
    Type_choice = (
        ('up', 'Upvote'),
        ('down','Downvote')
    )
    owner = models.ForeignKey(Profile, on_delete=models.CASCADE , null = True,blank=True)
    comment = models.TextField(max_length=500,blank=False,null=False)
    project = models.ForeignKey(Project , on_delete=models.CASCADE)
    value = models.CharField(choices=Type_choice, max_length=100)
    created = models.DateTimeField(auto_now_add=True)
   
    class Meta:
        unique_together = [["owner", "project"]]
        
    def __str__(self):
        return self.value
    
class Tag(models.Model):
    name = models.CharField(blank=False, null=False, max_length=50)
    added = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name
    
