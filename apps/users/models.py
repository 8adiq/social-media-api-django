from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    username = models.TextField(unique=True)
    email = models.EmailField(unique=True)
    bio = models.TextField(blank=True,null=True)
    profile_picture = models.ImageField(upload_to='profile_pics/',blank=True,null=True)



    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']


    def __str__(self):
        return self.email
