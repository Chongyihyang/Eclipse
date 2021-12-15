from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    title=models.CharField(blank=False,null=False, max_length=200,default=None)
    description=models.TextField(blank=True,  null=True, max_length=2000)
    created_time=models.DateTimeField(auto_now=True)
    user=models.ForeignKey(User, on_delete=models.CASCADE, related_name="Post", null=False) 

class Image(models.Model):
    post=models.ForeignKey(Post,models.CASCADE,null=True,blank=True)
    image=models.ImageField(verbose_name="image",upload_to="media",null=True,blank=True)

class Video(models.Model):
    post=models.ForeignKey(Post,models.CASCADE,null=True,blank=True)
    video=models.FileField(verbose_name="video",upload_to="media",null=True,blank=True)

class Comment(models.Model):
    post=models.ForeignKey(Post,models.CASCADE,null=True,blank=True)
    user=models.ForeignKey(User, on_delete=models.CASCADE, related_name="comment", null=False)
    comment=models.TextField(blank=False,  null=False, max_length=500)
    created_time_comments=models.DateTimeField(auto_now=True)

    class Meta:
        ordering=['comment']