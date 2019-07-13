from django.db import models
from django.utils import timezone
import datetime
from django.urls import reverse
# Create your models here.

class Post(models.Model):
    post_image = models.ImageField('img', upload_to='static/meme_review', blank=True)
    caption = models.TextField(max_length=200)
    pub = models.DateTimeField()

class Comment(models.Model):
    name = models.TextField(max_length=200)
    comment = models.TextField()
    published_date = models.DateTimeField()
    for_post = models.ForeignKey(Post, on_delete=models.CASCADE)
