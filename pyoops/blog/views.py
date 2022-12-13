from django.shortcuts import render
from .models import blog_post

posts = blog_post.objects.all()


def blog_posts_list(request):
    tags = {}
    for tag in posts:
        tags[tag.title] = [tag for tag in tag.tags.all()]

    return render(request, 'blog_posts_list.html',{'posts':posts.exclude(body="*"),'tags':tags})

def blog_single_post(request, techtitle):
    for post in posts:
        if post.tech_title == techtitle:
            comments = post.comments.all()
            single_blog_post_tags = post.tags.all()
            post.views = post.views+1
            post.save()
            post_data = post
        else: pass    
    return render(request, 'blog_post_single.html',{
        'post_data':post_data,'comments':comments, "tags": single_blog_post_tags})    
