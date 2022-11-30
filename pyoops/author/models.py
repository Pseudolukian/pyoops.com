from django.db import models
from pyoops.settings import user_uploads_avatars_dir




class author(models.Model):
    #Main info
    nickname = models.CharField(max_length=20)
    avatar = models.ImageField(upload_to = user_uploads_avatars_dir, blank=True, null=True)
    headline = models.TextField(max_length=200, blank=True)
    speciality = models.CharField(max_length=50, blank=True)
    #blog_posts = models.ManyToManyField(blog_post, on_delete=models.CASCADE)
    
    #Social media links
    email = models.EmailField(max_length=50, blank=True, null=True)
    facebook = models.CharField(max_length=100, blank=True, null=True)
    twitter = models.CharField(max_length=100, blank=True, null=True)
    linkedin = models.CharField(max_length=100, blank=True, null=True)
    
    #Auto generation data
    registration = models.DateTimeField(auto_now_add=True)
    
    #forum_posts

    def __str__(self):
        return self.nickname