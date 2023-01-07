import uuid
from django.db import models
from author.models import author
from pyoops.settings import users_static_data, admin_static_data



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
    author = models.ForeignKey(author, on_delete=models.CASCADE,blank=False)
    title = models.CharField(max_length=100, blank=False)
    tech_title = models.CharField(max_length=100, blank=False)
    cover = models.ImageField(upload_to = users_static_data + 'blog_post_covers', blank=False)
    preview = models.TextField(blank=False)
    body = models.TextField(blank=False)
    category = models.ForeignKey('blog_post_category', on_delete=models.CASCADE,blank=False)
    tags = models.ManyToManyField('blog_tag', blank=False)
    level = models.ForeignKey('blog_post_level', blank=False, null=True, on_delete=models.CASCADE)
    thread = models.ManyToManyField('self', blank=False, symmetrical=False)

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
    post = models.ForeignKey(blog_post, blank=False, on_delete=models.CASCADE, null=True)
    
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