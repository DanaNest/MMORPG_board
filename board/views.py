from django import forms
from django.shortcuts import redirect, render, get_object_or_404
from django.views.generic import ListView, DetailView

from .forms import PostForm
from .models import User, Post, Reply


class PostList(ListView):
    model = Post
    template_name = 'posts.html'
    context_object_name = 'posts'
    ordering = '-data_creation'
    paginate_by = 10  # вывод 10 записей на страницу


class PostDetail(DetailView):
    model = Post
    template_name = 'post.html'
    context_object_name = 'post'


def add_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post_item = form.save(commit=False)
            post_item.request = request
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


def delete_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)

    if request.method == 'POST':
        post.delete()
        return redirect('posts')

    return render(request, 'confirm_delete.html', {'post': post})

#Reply