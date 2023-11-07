from django.forms import ModelForm
from .models import Post


class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = [
            'category',
            'title',
            'content2',
            'content',
            'author'
        ]

