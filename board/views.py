from django import forms
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render, get_object_or_404
from django.views.generic import ListView, DetailView
from requests import post

from .forms import PostForm, ResponseForm
from .models import Post, Response


class PostList(ListView):                          # список объявлений
    model = Post
    template_name = 'posts.html'
    context_object_name = 'posts'
    ordering = '-data_creation'
    paginate_by = 10  # вывод 10 записей на страницу


class PostDetail(DetailView):                      # детали объявления
    model = Post
    template_name = 'post.html'
    context_object_name = 'post'
    pk_url_kwarg = 'post_id'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        post = self.get_object()
        responses = Response.objects.filter(post=post)
        context['responses'] = responses
        return context


def add_post(request):                           # создать объявление
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


def edit_post(request, post_id=None):            # редактировать объявление
    item = get_object_or_404(Post, id=post_id)
    form = PostForm(request.POST or None, instance=item)
    if form.is_valid():
        form.save()
        return redirect('posts')
    return render(request, 'post_form.html', {'form': form})


def delete_post(request, post_id):              # удалить объявление
    post = get_object_or_404(Post, id=post_id)

    if request.method == 'POST':
        post.delete()
        return redirect('posts')

    return render(request, 'confirm_delete.html', {'post': post})


@login_required
def create_response(request, post_id):
    post = get_object_or_404(Post, id=post_id)

    if request.method == 'POST':
        content = request.POST.get('content')
        response = Response(author=request.user, post=post, content=content)
        response.save()
        return HttpResponseRedirect('/posts/{}'.format(post_id))

    return render(request, 'create_response.html', {'post': post})

@login_required
def accept_response(request, response_id):
    response = get_object_or_404(Response, id=response_id)
    response.status = True
    response.save()
    return redirect('post', post_id=response.post.id)
