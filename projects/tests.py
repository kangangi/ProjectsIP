from django.test import TestCase
from .models import Project
from django.contrib.auth.models import User

# title = models.CharField(max_length = 30)
#     image = CloudinaryField('image')
#     description = models.TextField()
#     link = models.TextField()
#     profile = models.ForeignKey(User, on_delete=models.CASCADE)
class ProjectTestClass(TestCase):
    '''
    Class that tests the projects
    '''
    def setUp(self):
        '''
        Creates new instances before a test
        '''
        self.chombs = User(username="chombs", email="chombs@gmail.com", password = "12345")
        self.test = Project(title= "test", image = "image_url", description ="test project", link = "testlink", profile= self.chombs)

        self.chombs.save()
        self.test.save_project()

    def tearDown(self):
        '''
        Clears database after each test
        '''
        Project.objects.all().delete()

    def test_image_instance(self):
        '''
        This will test whether the new image created is an instance of the Image class
        '''
        self.assertTrue(isinstance(self.test, Project))

    def test_save_project_method(self):
        '''
        This tests whether new project is added to the db 
        '''
        self.test.save_project()
        projects = Project.objects.all()
        self.assertTrue(len(projects)> 0)

    def test_delete_project(self):
        '''
        This tests whether project is deleted
        '''
        self.test.save_project()
        projects1 = Project.objects.all()
        self.assertEqual(len(projects1),1)
        self.test.delete_project()
        projects2 = Project.objects.all()
        self.assertEqual(len(projects2),0)

    def test_display_projects(self):
        '''
        This tests whether all projects are displayed
        '''
        projects = Project.display_all_projects()
        self.assertTrue(len(projects) > 0 )






