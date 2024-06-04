from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import (CreateView, DeleteView, DetailView, ListView,
                                  UpdateView)

from plataforma.forms import PostForm
from plataforma.models import Post


class PostCreateView(CreateView):
    model = Post
    template_name = 'plataforma/post/post_create.html'
    fields = ['icon_user', 'name', 'data', 'hour', 'content', 'image_post']
    success_url = '/'

    def get(self, request):
        form_post = PostForm()
        return render(request, 'plataforma/post/post_create.html', {'form_post': form_post})


class PostUpdateView(UpdateView):
    model = Post
    template_name = 'plataforma/post/post_update.html'
    fields = ['icon_user', 'name', 'data', 'hour', 'content', 'image_post']
    success_url = '/'


class PostDeleteView(DeleteView):
    model = Post
    template_name = 'plataforma/post/post_delete.html'
    success_url = '/'


class PostDetailView(DetailView):
    model = Post
    template_name = 'plataforma/post/post_detail.html'
    context_object_name = 'post'


class PostListView(LoginRequiredMixin, ListView):
    model = Post
    template_name = 'plataforma/post/post_list.html'
    context_object_name = 'posts'
    paginate_by = 2

    def get_queryset(self):
        queryset = super().get_queryset()
        query = self.request.GET.get('q')
        if query:
            queryset = queryset.filter(title__icontains=query)
            print(queryset.query)
        orderby = self.request.GET.get('pub_date', 'name')
        return queryset.order_by(orderby)
