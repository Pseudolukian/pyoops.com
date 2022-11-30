# Generated by Django 4.1.3 on 2022-11-30 13:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='news',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_created=True)),
                ('title', models.CharField(max_length=100)),
                ('preview', models.TextField(max_length=300)),
                ('cover', models.ImageField(upload_to='static/news_uploads_files')),
                ('body', models.TextField()),
            ],
        ),
    ]
