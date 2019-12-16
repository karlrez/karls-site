from django.db import models

# Create your models here.
class MemeUpload(models.Model):
    user = models.CharField(max_length=50)
    description = models.CharField(max_length=100)
    image = models.ImageField(upload_to='media/uploads')
    pub_date = models.DateTimeField(auto_now_add=True)

#class Comment(models.Model):
    #post = models.ForeignKey(MemeUpload, related_name='comments', on_delete=models.CASCADE)
    #user = models.CharField(max_length=50)
    #description = models.TextField(max_length=100)
    #created = models.DateTimeField(auto_now_add=True)
