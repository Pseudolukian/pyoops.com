import uuid
from django.db import models
from pyoops.settings import admin_static_data



class news(models.Model):
    title = models.CharField(max_length=100)
    preview = models.TextField(max_length=300)
    cover = models.ImageField(upload_to = admin_static_data + 'news_cover')
    body = models.TextField()
    date = models.DateTimeField(auto_created=True)
    id = models.UUIDField(default = uuid.uuid4, unique=True, primary_key=True, editable=False)

    def __str__(self):
        return self.title

