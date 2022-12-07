from django.contrib import admin
from .models import blog_post, blog_tag, blog_comment, blog_post_category, blog_post_level

admin.site.register(blog_post)
admin.site.register(blog_tag)
admin.site.register(blog_comment)
admin.site.register(blog_post_category)
admin.site.register(blog_post_level)