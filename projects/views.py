from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .models import Project
from .forms import AddProjectForm

def index(request):
    '''
    Displays landing page 
    '''
    title = "IPDb"
    projects = Project.display_all_projects()

    return render(request,"index.html",{"title": title, "projects": projects})

@login_required(login_url="/accounts/login/")
def post_project(request):
    '''
    Enables a User to post a project
    '''
    if request.method == "POST":
        form = AddProjectForm(request.POST, request.FILES)
        if form.is_valid():
            project = form.save(commit= False)
            project.profile = request.user
            project.save()

        return redirect("index")
    else:
        form = AddProjectForm()

    return render(request, 'post_project.html', {"form": form})

