from django.forms import ModelForm
from django import forms
from .models import Project,Reviews
class ProjectForm(ModelForm):
    class Meta:
        model= Project
        fields= ['name','description','link','tag','image']
        widgets = {
            'tag': forms.CheckboxSelectMultiple
        }

class ReviewForm(ModelForm):
    class Meta:
        model = Reviews
        fields =['comment','value']
    
            
        