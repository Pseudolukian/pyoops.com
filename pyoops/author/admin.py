from django.contrib import admin
from .models import author, skill_level, user_class

admin.site.register(author)
admin.site.register(skill_level)
admin.site.register(user_class)
