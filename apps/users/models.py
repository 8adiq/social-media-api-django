from django.db import models
from django.contrib.auth.models import AbstractUser



class User(AbstractUser):
    email = models.EmailField(unique=True)
    bio = models.TextField(blank=True,null=True)
    profile_pic= models.ImageField(upload_to='',blank=True,null=True)


    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['firstname','lastname','username']

    def __str__(self):
        return f' Email: {self.email}, Username: {self.username}'
