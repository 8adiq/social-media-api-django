from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.

User = get_user_model()

class Post(models.Model):
    username = models.ForeignKey(User, on_delete=models.CASCADE,related_name='posts',default=1)
    text = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='post_images/',blank=True,null=True)
    video = models.FileField(upload_to='post_videos/',blank=True,null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta():
        ordering = ['created_at']

    def __str__(self):
        return f'Post by {self.username} at {self.created_at}'