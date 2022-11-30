from django.db import models
from author.models import author
from pyoops.settings import user_uploads_post_files

class blog_post(models.Model):
    author = models.ForeignKey(author, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    tech_title = models.CharField(max_length=100)
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    cover = models.ImageField(upload_to = user_uploads_post_files)
    preview = models.TextField()
    tags = models.ManyToManyField("blog_tag")
    views= models.IntegerField(default=0)
    #thread
    #comments

    def __str__(self):
        return self.title

class blog_comment(models.Model):
    
    comment=models.TextField()
    author=models.ForeignKey(author, on_delete=models.CASCADE)
    post=models.ForeignKey(blog_post, on_delete=models.CASCADE)
    data = models.DateTimeField(auto_now_add=True)       

class blog_tag(models.Model):
    atomic = False
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name     