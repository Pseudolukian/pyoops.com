from django.shortcuts import render, redirect
from .models import blog_post, blog_comment
from .forms import create_post, create_comment

posts = blog_post.objects.all()
post_comments = blog_comment.objects.all()

def blog_posts_list(request):
    tags = {}
    for tag in posts:
        tags[tag.title] = [tag for tag in tag.tags.all()]
    return render(request, 'blog_posts_list.html',{'posts':posts.exclude(body="*"),'tags':tags})


def blog_single_post(request, techtitle):
    comment_form = create_comment()
    post_data = posts.get(tech_title = techtitle)
    post_data.views = post_data.views+1
    title = post_data.title
    single_blog_post_tags = post_data.tags.all()
    comments = [comment for comment in post_comments if str(comment.post) == title]  
    
    if request.method == "POST":
        comment_form = create_comment(request.POST)
        if comment_form.is_valid():
            comment_form.save()
            return redirect("/blog/" + techtitle)
    
    return render(request, 'blog_post_single.html',
    {"post_data":post_data,"tags": single_blog_post_tags,
    "comments":comments,"form":comment_form})             
     
def post_add(request):
    form = create_post()
    if request.method == "POST":
        form = create_post(request.POST)
        print(form.is_valid())
        if form.is_valid():
            print("Add new post")
            form.save()
            return redirect("/blog/")
    return(render(request, "create_post.html", {"form":form}))
    
