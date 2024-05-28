from django.http import HttpResponse
from django.views.generic import (CreateView, DeleteView, DetailView, ListView,
                                  UpdateView)

from plataforma.models import Post

class PostCreateView(CreateView):
    model = Post
    template_name = 'post/post_create.html'
    fields = ['icon_user', 'name', 'data', 'hour', 'content', 'image_post']
    success_url = '/'

class PostUpdateView(UpdateView):
    model = Post
    template_name = 'post/post_update.html'
    fields = ['icon_user', 'name', 'data', 'hour', 'content', 'image_post']
    success_url = '/'

class PostDeleteView(DeleteView):
    model = Post
    template_name = 'post/post_delete.html'
    success_url = '/'

class PostDetailView(DetailView):
    model = Post
    template_name = 'post/post_detail.html'
    context_object_name = 'post'

class PostListView(ListView):
    model = Post
    template_name = 'post/post_list.html'
    context_object_name = 'posts'

    