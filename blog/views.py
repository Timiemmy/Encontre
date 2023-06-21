from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from django.views import View
from django.views.generic import ListView, DetailView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import Post
from .forms import PostForm


class Index(ListView):
    model = Post
    posts = Post.published.all().order_by('-publish_date')
    context_object_name = "posts"
    template_name = 'blog/index.html'
    paginate_by = 3


def add_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.created_date = timezone.now
            post.save()
            return redirect('detail_post', year=post.publish_date.year, month=post.publish_date.month, day=post.publish_date.day, post=post.slug)
    else:
        form = PostForm()
    return render(request, 'blog/blog_edit.html', {'form': form})


def post_detail(request, year, month, day, post):
    post = get_object_or_404(Post, status=Post.Status.PUBLISHED, slug=post,
                             publish_date__year=year, publish_date__month=month, publish_date__day=day)
    return render(request, "blog/blog_post.html", {"post": post})


def edit_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.created_date = timezone.now
            post.save()
            return redirect('detail_post', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/blog_edit.html', {'form': form})


class DeletePostView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    template_name = 'blog/blog_delete.html'
    success_url = reverse_lazy('index')

    def test_func(self):
        post = Post.objects.get(id=self.kwargs.get('pk'))
        return self.request.user.id == post.author.id
