from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm
from .models import Profile,Inbox
class RegisterForm(UserCreationForm):
    class Meta:
        model= User
        fields = ['first_name','username','password1','password2','email'] 
        
        def __init__(self, *args, **kwargs):
            super(UserCreationForm, self).__init__(*args, **kwargs)
            for visible in self.visible_fields():
                visible.field.widget.attrs['class'] = 'input'
                
class ProfileEditForm(ModelForm):
    class Meta:
        model = Profile
        fields = ['location','Profile_pic','shortbio','bio','social_github','social_linkedin','skills']
        
class sendMessageForm(ModelForm):
    class Meta:
        model= Inbox
        fields = ['content']