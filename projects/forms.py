from .models import Project
from django.forms import ModelForm

class AddProjectForm(ModelForm):
    class Meta:
        model = Project
        exclude = ['profile, pubdate']

        