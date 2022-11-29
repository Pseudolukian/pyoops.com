from django.db import models
from pyoops.settings import user_upload_dir



class author(models.Model):
    nickname = models.CharField(max_length=20)
    email = models.EmailField(max_length=50)
    avatar = models.ImageField(upload_to = user_upload_dir, blank=True, null=True)
    registration = models.DateTimeField(auto_now_add=True)
    #blog_posts
    #forum_posts

    def __str__(self):
        return self.nickname