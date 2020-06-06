from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name = "index"),
    path('post/project', views.post_project, name = "post_project"),
    path('post/<int:id>', views.project_details, name = "project_details"),
    path('search/', views.project_search, name = "project_search"),
    path('profile/',views.profile, name = "profile"),
    path('profile/edit/', views.edit_profile,name= 'edit_profile'),

]