from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import (CreateView, DeleteView, DetailView, ListView,
                                  UpdateView)

from plataforma.forms import ChatForm
from plataforma.models import Chat


class ChatCreateView(CreateView):
    model = Chat
    template_name = 'plataforma/chat/chat_create.html'
    fields = ['name', 'icon_user']
    success_url = '/'

    def get(self, request):
        form_chat = ChatForm()
        return render(request, 'plataforma/chat/chat_create.html', {'form_chat': form_chat})


class ChatUpdateView(UpdateView):
    model = Chat
    template_name = 'plataforma/chat/chat_update.html'
    fields = ['name', 'icon_user']
    success_url = '/'


class ChatDeleteView(DeleteView):
    model = Chat
    template_name = 'plataforma/chat/chat_delete.html'
    success_url = '/'


class ChatDetailView(LoginRequiredMixin, DetailView):
    model = Chat
    template_name = 'plataforma/chat/chat_detail.html'
    context_object_name = 'chat'


class ChatListView(ListView):
    model = Chat
    template_name = 'plataforma/chat/chat_list.html'
    context_object_name = 'chats'
    paginate_by = 2

    def get_queryset(self):
        queryset = super().get_queryset()
        query = self.request.GET.get('q')
        if query:
            queryset = queryset.filter(title__icontains=query)
            print(queryset.query)
        orderby = self.request.GET.get('pub_date', 'name')
        return queryset.order_by(orderby)
