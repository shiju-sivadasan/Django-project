from django.db import models

# Create your models here.
class Details(models.Model):
    about=models.TextField()
    projects=models.TextField()
    experience=models.TextField()
    education=models.TextField()
    certifications=models.TextField()
    def __str__(self):
        return self.about