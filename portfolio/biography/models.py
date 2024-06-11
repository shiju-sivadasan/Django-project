from django.db import models

# Create your models here.
class Biography(models.Model):
    name=models.CharField(max_length=200)
    img=models.ImageField(upload_to='profile_pics/')
    date_of_birth=models.DateField()
    gender=models.CharField(max_length=200)
    marital_status=models.CharField(max_length=200)
    nationality=models.CharField(max_length=200)
    skills=models.TextField()
    address=models.TextField()
    email=models.CharField(max_length=200)
    phone=models.CharField(max_length=200)
    linkedin=models.CharField(max_length=200)

    def __str__(self):
        return self.name