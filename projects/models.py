from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

class Project(models.Model):
    '''
    Class that defines the project objects
    '''
    title = models.CharField(max_length = 30)
    image = CloudinaryField('image')
    description = models.TextField()
    link = models.TextField()
    profile = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

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
