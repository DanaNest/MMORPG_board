from django import forms
from django.shortcuts import redirect, render, get_object_or_404
from django.views.generic import ListView, DetailView

from .forms import PostForm
from .models import User, Post, Reply


def add_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post_item = form.save(commit=False)
            post_item.save()
            return redirect('posts')
    else:
        form = PostForm()
    return render(request, 'post_form.html', {'form': form})


def edit_post(request, post_id=None):
    item = get_object_or_404(Post, id=post_id)
    form = PostForm(request.POST or None, instance=item)
    if form.is_valid():
        form.save()
        return redirect('posts')
    return render(request, 'post_form.html', {'form': form})

class UserRegistrationForm(forms.Form):
    email = forms.EmailField()


class AuthorRegistrationForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['email']


class PostList(ListView):
    model = Post
    # ordering = '-data_creation'
    template_name = 'posts.html'
    context_object_name = 'posts'
    ordering = '-data_creation'
    paginate_by = 10  # вывод 10 записей на страницу


class PostDetail(DetailView):
    model = Post
    template_name = 'post.html'
    context_object_name = 'post'

# class PostCreationForm(forms.ModelForm):
#     class Meta:
#         model = Post
#         fields = ['author', 'category', 'title', 'content']
#
#
# class PostEditForm(forms.ModelForm):
#     class Meta:
#         model = Post
#         fields = ['category', 'title', 'content']
#
#
# class ReplyCreationForm(forms.ModelForm):
#     class Meta:
#         model = Reply
#         fields = ['author', 'post', 'text']
#
#
# class ReplyEditForm(forms.ModelForm):
#     class Meta:
#         model = Reply
#         fields = ['text']
