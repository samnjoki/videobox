from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Box(models.Model):
    title=models.CharField(max_length=255)
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return f'{self.title}'

class video(models.Model):
    title=models.CharField(max_length=255)
    url=models.URLField()
    youtube_id=models.CharField(max_length=255)
    box=models.ForeignKey(Box,on_delete=models.CASCADE)