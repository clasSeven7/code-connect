from django.http import HttpResponse
from django.views.generic import (CreateView, DeleteView, DetailView, ListView,
                                  UpdateView)

from plataforma.models import Chat


class ChatCreateView(CreateView):
    model = Chat
    template_name = 'plataforma/chat/chat_create.html'
    fields = ['name', 'icon_user']
    success_url = '/'


class ChatUpdateView(UpdateView):
    model = Chat
    template_name = 'plataforma/chat/chat_update.html'
    fields = ['name', 'icon_user']
    success_url = '/'


class ChatDeleteView(DeleteView):
    model = Chat
    template_name = 'plataforma/chat/chat_delete.html'
    success_url = '/'


class ChatDetailView(DetailView):
    model = Chat
    template_name = 'plataforma/chat/chat_detail.html'
    context_object_name = 'chat'


class ChatListView(ListView):
    model = Chat
    template_name = 'plataforma/chat/chat_list.html'
    context_object_name = 'chats'
