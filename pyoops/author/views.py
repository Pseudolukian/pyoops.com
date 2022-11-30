from django.shortcuts import render
from django.http import request
from .models import author

authors = author.objects.all()

def author_list(request):
    return render(request, 'authors.html', {'authors':authors})

