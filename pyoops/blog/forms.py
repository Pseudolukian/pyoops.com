from django.forms import ModelForm
from .models import blog_post, blog_comment


class create_post(ModelForm):
    class Meta:
        model = blog_post
        fields = ["title","tech_title","cover","preview","body"]

class create_comment(ModelForm):
    class Meta:
        model = blog_comment
        fields = "__all__"

