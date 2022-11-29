from django.contrib import admin
from .models import blog_post,tag

admin.site.register(blog_post)
admin.site.register(tag)
