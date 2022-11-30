from django.contrib import admin
from .models import blog_post, blog_tag, blog_comment

admin.site.register(blog_post)
admin.site.register(blog_tag)
admin.site.register(blog_comment)

