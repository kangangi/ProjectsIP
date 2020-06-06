from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .models import Project,Profile
from .forms import AddProjectForm, RateForm
from django.urls import reverse
from django.http import HttpResponseRedirect

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

def project_details(request,id):
    '''
    Show project details
    '''
    project = Project.objects.get(pk = id)
    if request.method == "POST":
        form = RateForm(request.POST)
        if form.is_valid():
            design = form.cleaned_data['design']
            usability = form.cleaned_data['usability']
            content = form.cleaned_data['content']

            new_score = (design + usability + content)/3
            project.scores = project.scores + new_score
            project.save()

            return HttpResponseRedirect(reverse('project_details',args =[int(project.id)]))

    else:
        form = RateForm()
    return render(request, 'project_details.html', {"project":project, "form": form})

def project_search(request):
    '''
    Display search results
    '''
    if "project" in request.GET and request.GET["project"]:
        searched_project = request.GET.get("project")
        projects = Project.search_project(searched_project)
        message =f"{searched_project}"
       
        
        return render(request, 'search.html', {"projects": projects,"message": message})
    else:
        message = "You haven't searched for any term"
        return render(request,'search.html', {"message": message}) 

def profile(request):
    '''
    Displays User's profile page
    '''
    title = 'Profile'
    current_user = request.user
    profile = Profile.objects.get(user =current_user)

    return render(request, 'profile.html', {'profile':profile})
    