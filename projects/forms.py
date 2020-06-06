from .models import Project
from django.forms import ModelForm
from django import forms

class AddProjectForm(ModelForm):
    class Meta:
        model = Project
        exclude = ['profile, pubdate']


    
class RateForm(forms.Form):
    design = forms.IntegerField()
    usability = forms.IntegerField()
    content = forms.IntegerField()