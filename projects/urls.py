from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name = "index"),
    path('post/project', views.post_project, name = "post_project"),
    path('post/<int:id>', views.project_details, name = "project_details"),
    # path('post/rate/<int:id>',views.rate_project, name ="rate_project"),
]