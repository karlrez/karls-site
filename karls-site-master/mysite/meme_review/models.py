from django.db import models
from django.urls import reverse

# Create your models here.
class MemeUpload(models.Model):
    user = models.CharField(max_length=50)
    description = models.CharField(max_length=100)
    image = models.ImageField(upload_to='media/uploads')
    pub_date = models.DateTimeField(auto_now_add=True)

class Comment(models.Model):
    post = models.ForeignKey(MemeUpload, related_name='comments', on_delete=models.CASCADE) # relationship to the parent memeUpload object
    user = models.CharField(max_length=50)
    description = models.TextField(max_length=150)
    created = models.DateTimeField(auto_now_add=True)
