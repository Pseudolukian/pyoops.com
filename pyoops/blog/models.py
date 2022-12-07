import uuid
from django.db import models
from author.models import author
from pyoops.settings import users_static_data, admin_static_data
from colorfield.fields import ColorField



class blog_post_category(models.Model):
    #Main fields
    tags = models.ManyToManyField('blog_tag')
    category = models.CharField(max_length=100, null=True, blank=True)
    icon = models.ImageField(upload_to = admin_static_data + 'blog_post_category_icons')
    id = models.UUIDField(default = uuid.uuid4, unique=True, primary_key=True, editable=False)

    def __str__(self):
        return self.category 

class blog_tag(models.Model):
    #Main fields
    name = models.CharField(max_length=50)
    #color = ColorField(default='#FF0000')

    #Autofill fields
    id = models.UUIDField(default = uuid.uuid4, unique=True, primary_key=True, editable=False)

    def __str__(self):
        return self.name     

class blog_post(models.Model):
    #Main fields
    author = models.ForeignKey(author, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    tech_title = models.CharField(max_length=100)
    cover = models.ImageField(upload_to = users_static_data + 'blog_post_covers')
    preview = models.TextField()
    body = models.TextField()
    category = models.ForeignKey('blog_post_category', on_delete=models.CASCADE)
    tags = models.ManyToManyField('blog_tag', blank=True)
    level = models.ForeignKey('blog_post_level', blank=True, null=True, on_delete=models.CASCADE)
    thread = models.ManyToManyField('self', blank=True, symmetrical=False)
    comments = models.ManyToManyField('blog_comment')

    #Autofill fields
    views= models.IntegerField(default=0)
    date = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default = uuid.uuid4, unique=True, primary_key=True, editable=False)
    
    def __str__(self):
        return self.title

class blog_comment(models.Model):
    #Main fields
    author = models.ForeignKey(author, on_delete=models.CASCADE, null=True)
    comment = models.TextField()
    
    #Autofill fields
    data = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default = uuid.uuid4, unique=True, primary_key=True, editable=False)  

    def __str__(self):
        return self.comment


class blog_post_level(models.Model):
    #Main fields
    level = models.CharField(max_length=100)
    icon = models.ImageField(upload_to = admin_static_data + 'blog_post_level_icons')

    #Autofill fields
    id = models.UUIDField(default = uuid.uuid4, unique=True, primary_key=True, editable=False)

    def __str__(self):
        return self.level