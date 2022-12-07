from django.shortcuts import render
from django.http import request
from .models import author

authors = author.objects.all()

def author_list(request):
    return render(request, 'authors.html', {'authors':authors})

def author_homepage(request, nick):
    author = authors.filter(nickname = nick)
    user_class = [[x for x in u_c.user_class.all()] 
                for u_c in author.prefetch_related('user_class')]
    
    return render(request,'author_homepage.html', 
    {'author_data':author,'user_class':user_class})