from django.db import models

class Post(models.Model):
    username = models.CharField(max_length=255)
    photo = models.FileField(upload_to="static/upload/",default="")
    content = models.CharField(max_length=255)
    like = models.IntegerField(default=0)
    dislike = models.IntegerField(default=0)

# Create your models here.
