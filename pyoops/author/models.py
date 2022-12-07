import uuid
from django.db import models
from pyoops.settings import users_static_data, admin_static_data



class author(models.Model):
    #Main info
    nickname = models.CharField(max_length=50, unique=True)
    avatar = models.ImageField(upload_to = users_static_data + 'author_avatar', blank=True, null=True)
    headline = models.TextField(max_length=200, blank=True)
    speciality = models.CharField(max_length=50, blank=True)
    skill = models.ForeignKey('skill_level', on_delete=models.CASCADE, blank=True, null=True)
    bio = models.TextField(blank=True)
    
    #Social media links
    email = models.EmailField(max_length=50, blank=True, null=True)
    facebook = models.CharField(max_length=100, blank=True, null=True, default='http://facebook.com')
    twitter = models.CharField(max_length=100, blank=True, null=True, default='http://twitter.com')
    linkedin = models.CharField(max_length=100, blank=True, null=True, default='http://linked.com')
    
    #Auto generation data
    registration = models.DateTimeField(auto_now_add=True)
    user_class = models.ManyToManyField('user_class', blank=True)
    id = models.UUIDField(default = uuid.uuid4, unique=True, primary_key=True, editable=False)
    #fallowers

    def __str__(self):
        return self.nickname

class skill_level(models.Model):
    skill_level = models.CharField (max_length=50, blank=True, null=True)
    skill_icon = models.ImageField(upload_to = admin_static_data + 'skill_level_icon', blank=True, null=True)
    id = models.UUIDField(default = uuid.uuid4, unique=True, primary_key=True, editable=False)           

    def __str__(self):
        return self.skill_level

class user_class(models.Model):
    user_class = models.CharField(max_length=100, null=True, blank=True)
    id = models.UUIDField(default = uuid.uuid4, unique=True, primary_key=True, editable=False)

    def __str__(self):
        return self.user_class
