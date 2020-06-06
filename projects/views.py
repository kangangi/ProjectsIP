from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required()
def index(request):
    '''
    Displays landing page 
    '''
    title = "IPDb"

    return render(request,"index.html",{"title": title})


