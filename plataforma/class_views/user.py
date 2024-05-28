from django.http import HttpResponse
from django.views.generic import (CreateView, DeleteView, DetailView, ListView,
                                  UpdateView)


from plataforma.models import User


class UserCreateView(CreateView):
    model = User
    template_name = 'user/user_create.html'
    fields = ['name', 'email', 'password', 'icon_user', 'status']
    success_url = '/'

class UserUpdateView(UpdateView):
    model = User
    template_name = 'user/user_update.html'
    fields = ['name', 'email', 'password', 'icon_user', 'status']
    success_url = '/'

class UserDeleteView(DeleteView):
    model = User
    template_name = 'user/user_delete.html'
    success_url = '/'

class UserDetailView(DetailView):
    model = User
    template_name = 'user/user_detail.html'
    context_object_name = 'user'

class UserListView(ListView):
    model = User
    template_name = 'user/user_list.html'
    context_object_name = 'users'


    