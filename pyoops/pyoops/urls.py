"""pyoops URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from author.views import author_list, author_homepage
from blog.views import blog_posts_list, blog_single_post

urlpatterns = [
    path('admin/doc/', include('django.contrib.admindocs.urls')),
    path('admin/', admin.site.urls),
    path('authors/', author_list, name='authors'),
    path('author/<str:nick>', author_homepage, name='author_homepage'),
    path('blog/', blog_posts_list, name = 'blog'),
    path('blog/<str:techtitle>', blog_single_post, name = 'blog'),
]
