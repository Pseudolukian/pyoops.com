from django.db import models
from author.models import author
from pyoops.settings import user_upload_dir



class blog_post(models.Model):
    author = models.ForeignKey(author, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    tech_title = models.CharField(max_length=100)
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    cover = models.ImageField(upload_to = user_upload_dir)
    preview = models.TextField()
    tags = models.ManyToManyField("tag")
    #comments
    #views
    #thread

    def __str__(self):
        return self.title

class tag(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name