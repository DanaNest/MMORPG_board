from django.conf.urls.static import static
from django.urls import path, include
from django.shortcuts import redirect

from MMORPG import settings
from board import views
from board.views import PostList, PostDetail

urlpatterns = [
    path('', PostList.as_view(), name='index'),
    path('posts/', PostList.as_view(), name='posts'),
    path('posts/<int:pk>/', PostDetail.as_view(), name='post'),
    path('posts/add/', views.add_post, name='add_post'),
    path('posts/edit/<int:post_id>/', views.edit_post, name='edit_post'),
    path('posts/delete/<int:post_id>/', views.delete_post, name='delete_post'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
