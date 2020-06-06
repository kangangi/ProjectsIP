from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from django.db.models.signals import post_save
from django.dispatch import receiver


class Project(models.Model):
    '''
    Class that defines the project objects
    '''
    title = models.CharField(max_length = 30)
    image = CloudinaryField('image')
    description = models.TextField()
    link = models.TextField()
    profile = models.ForeignKey(User, on_delete=models.CASCADE)
    pubdate = models.DateTimeField(auto_now_add=True, null = True)
    scores = models.IntegerField(default=0)

    def __str__(self):
        return self.title


    def save_project(self):
        self.save()

    def delete_project(self):
        self.delete()

    @classmethod
    def display_all_projects(cls):
        return cls.objects.all()

    @classmethod 
    def search_project(cls,name):
        return Project.objects.filter(title__icontains = name)

class Profile(models.Model):
    '''
    Class that defines the profile objects
    '''
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    bio = models.TextField()
    picture = CloudinaryField('image')
    email = models.EmailField()
    github_link = models.TextField()

    def __str__(self):
        return self.user.username 

@receiver(post_save, sender = User)
def create_profile(sender, instance,created, **kwargs):
     if created:
        Profile.objects.create(user = instance)

@receiver(post_save,sender = User)
def save_profile( sender, instance, **kwargs):
    instance.profile.save()
