from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Project

def index(request):
    '''
    Displays landing page 
    '''
    title = "IPDb"
    projects = Project.display_all_projects()

    return render(request,"index.html",{"title": title, "projects": projects})


