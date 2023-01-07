from django.contrib import admin
from django.urls import path, include
from author.views import author_list, author_homepage
from blog.views import blog_posts_list, blog_single_post, post_add

urlpatterns = [
    path('admin/doc/', include('django.contrib.admindocs.urls')),
    path('admin/', admin.site.urls),
    path('authors/', author_list, name='authors'),
    path('author/<str:nick>', author_homepage, name='author_homepage'),
    path('blog/', blog_posts_list, name = 'blog'),
    path('blog/<str:techtitle>', blog_single_post, name = 'blog'),
    path('blog/post_add', post_add, name = 'blog_post_add'), 
]
