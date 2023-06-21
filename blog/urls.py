from django.urls import path, include
from .views import Index, DeletePostView, add_post, post_detail, edit_post

urlpatterns = [
    path('', Index.as_view(), name='index'),
    path('post/new/', add_post, name='new_post'),
    path('<int:year>/<int:month>/<int:day>/<slug:post>/',
         post_detail, name='detail_post'),
    path('post/<slug:post>/edit', edit_post, name='update_post'),
    path('<int:pk>/delete', DeletePostView.as_view(), name='delete_post'),
]
