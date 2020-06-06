from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name = "index"),
    path('post/project', views.post_project, name = "post_project"),
    
]