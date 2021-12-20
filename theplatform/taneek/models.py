from django.db import models
from django.conf import settings
from django.contrib.auth.models import User

class Posts(models.Model):
    title = models.CharField(max_length=200,null=True,blank=True)
    imageuploader_profile = models.ForeignKey(User, on_delete=models.CASCADE,null='True', blank=True)
    post_img = models.FileField(upload_to='media/', null=True,blank=True)
    description = models.CharField(max_length=200,null=True,blank=True)

class Details(models.Model):
    phone_id = models.ForeignKey(User, on_delete=models.CASCADE,null=True,blank=True)
    First = models.CharField(max_length=200,null=True,blank=True)
    Last = models.CharField(max_length=200,null=True,blank=True)
    work = models.CharField(max_length=200,null=True,blank=True)
    Excellence = models.CharField(max_length=200,null=True,blank=True)
    More = models.CharField(max_length=200,null=True,blank=True)

class displayusername(models.Model):
    username = models.CharField(max_length=200,null=True,blank=True)
    mobile = models.IntegerField(null=True,blank=True)
    email = models.CharField(max_length=200,null=True,blank=True)

class ConnectedUser(models.Model):
    username = models.CharField(max_length=200,null=True,blank=True)
    first_name = models.CharField(max_length=100, null=True,blank=True)
    email = models.CharField(max_length=200,null=True,blank=True)
    status = models.CharField(max_length=200,null=True,blank=True)