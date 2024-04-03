from distutils.command.upload import upload
from statistics import mode
import uuid
from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

AGE_CHOICES=(
    ("ALL","ALL"),
    ("KIDS","KIDS")
)
MOVIE_TYPE=(
    ("single","Single"),
    ("seasonal","Seasonal")
)
class Profile(models.Model):
    name=models.CharField(max_length=300)
    age_limits=models.CharField(max_length=5,choices=AGE_CHOICES)
    uuid=models.UUIDField(default=uuid.uuid4,unique=True)

class CustomUser(AbstractUser):
    profiles=models.ManyToManyField(Profile,blank=True)

class Video(models.Model):
    title:str = models.CharField(max_length=225,blank=True,null=True)
    file=models.FileField(upload_to='movies')
    
class Movie(models.Model):
    title=models.CharField(max_length=200)
    describtion=models.TextField()
    created=models.DateTimeField(auto_now_add=True)
    uuid=models.UUIDField(default=uuid.uuid4,unique=True)
    type=models.CharField(max_length=10,choices=MOVIE_TYPE)
    age_limits=models.CharField(max_length=5,choices=AGE_CHOICES,null=True,blank=True)
    image=models.ImageField(upload_to="images", null=True, blank=True)
    videos=models.ManyToManyField(Video)    