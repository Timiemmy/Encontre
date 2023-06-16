from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import ListView, DetailView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import Post

class Index(ListView):
	model = Post
	queryset = Post.objects.all().order_by('-date')
	template_name = 'blog/index.html'
	paginate_by = 1

class DetailPostView(DetailView):
	model = Post
	template_name = 'blog/blog_post.html'

	def get_context_data(self, *args, **kwargs):
		context = super(DetailPostView, self).get_context_data(*args, **kwargs)
		context['liked_by_user'] = False
		post = Post.objects.get(id=self.kwargs.get('pk'))
		if post.likes.filter(pk=self.request.user.id).exists():
			context['liked_by_user'] = True
		return context

class LikePost(View):
	def post(self, request, pk):
		post = Post.objects.get(id=pk)
		if post.likes.filter(pk=self.request.user.id).exists():
			post.likes.remove(request.user.id)
		else:
			post.likes.add(request.user.id)

		post.save()
		return redirect('detail_post', pk)

class DeletePostView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
	model = Post
	template_name = 'blog/blog_delete.html'
	success_url = reverse_lazy('index')

	def test_func(self):
		post = Post.objects.get(id=self.kwargs.get('pk'))
		return self.request.user.id == post.author.id