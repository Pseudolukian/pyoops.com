from django.shortcuts import render
from django.http import request
from .models import author
from blog.models import blog_post

authors = author.objects.all()
posts = blog_post.objects.all().exclude(body = "*")

def author_list(request):
    return render(request, 'authors.html', {'authors':authors})

def author_homepage(request, nick):
    author_posts = []
    author = authors.filter(nickname = nick)
    for post in posts:
        if post.author.nickname == nick:
            author_posts.append(post)
    return render(request,'author_homepage.html', 
    {'author_data':author,'author_posts':author_posts})