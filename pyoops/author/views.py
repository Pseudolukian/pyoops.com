from django.shortcuts import render
from django.http import request
from .models import author

authors = author.objects.all()

def author_list(request):
    return render(request, 'authors.html', {'authors':authors})

def author_homepage(request,nick):
    return render(request,'author_homepage.html', {'author_data':authors,'url_nick':nick} )