from django.db import models

# Create your models here.
class Project(models.Model):
    title=models.CharField(max_length=200)
    project_img=models.ImageField(upload_to="project_pics/")
    description=models.TextField()
    date=models.DateField()
    links=models.TextField()
    def __str__(self):
        return self.title