from django.db import models
from pyoops.settings import news_uploads_files

class news(models.Model):
    title = models.CharField(max_length=100)
    preview = models.TextField(max_length=300)
    cover = models.ImageField(upload_to = news_uploads_files)
    body = models.TextField()
    date = models.DateTimeField(auto_created=True)

    def __str__(self):
        return self.title

