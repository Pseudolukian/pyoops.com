from django.db import models
from author.models import author
from pyoops.settings import user_uploads_post_files
from colorfield.fields import ColorField

class blog_post(models.Model):
    #Main fields
    author = models.ForeignKey(author, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    tech_title = models.CharField(max_length=100)
    cover = models.ImageField(upload_to = user_uploads_post_files)
    preview = models.TextField()
    body = models.TextField()
    thread = models.ManyToManyField('self', blank=True, symmetrical=False)

    #Autofill fields
    views= models.IntegerField(default=0)
    date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title

class blog_comment(models.Model):
    #Main fields
    author = models.ForeignKey(author, on_delete=models.CASCADE, null=True)
    comment = models.TextField()
    post = models.ForeignKey(blog_post, on_delete=models.CASCADE, null=True)

    #Autofill fields
    data = models.DateTimeField(auto_now_add=True)       

    def __str__(self):
        return self.author

class blog_post_category(models.Model):
    #Main fields
    category = models.CharField(max_length=100)
    icon = models.ImageField(upload_to=user_uploads_post_files)
    post = models.OneToOneField(blog_post, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.category 

class blog_tag(models.Model):
    #Main fields
    name = models.CharField(max_length=50)
    category = models.ForeignKey(blog_post_category, on_delete=models.CASCADE, null=True)
    color = ColorField(default='#FF0000')

    def __str__(self):
        return self.name     

class blog_post_level(models.Model):
    #Main fields
    level = models.CharField(max_length=100)
    icon = models.ImageField(upload_to=user_uploads_post_files)

    def __str__(self):
        return self.level  