from django.urls import path, include
from .views import Index, DetailPostView, LikePost, DeletePostView, add_post, edit_post

urlpatterns = [
    path('', Index.as_view(), name='index'),
    path('post/new/', add_post, name='new_post'),
    path('<int:pk>/', DetailPostView.as_view(), name='detail_post'),
    path('post/<int:pk>/edit', edit_post, name='update_post'),
    path('<int:pk>/like', LikePost.as_view(), name='like_post'),
    path('<int:pk>/delete', DeletePostView.as_view(), name='delete_post')
]