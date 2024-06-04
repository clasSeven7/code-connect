from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import (CreateView, DeleteView, DetailView, ListView,
                                  UpdateView)

from plataforma.forms import EventForm
from plataforma.models import Event


class EventCreateView(CreateView):
    model = Event
    template_name = 'plataforma/event/event_create.html'
    fields = ['name', 'data', 'address']
    success_url = '/'

    def get(self, request):
        form_event = EventForm()
        return render(request, 'plataforma/event/event_create.html', {'form_event': form_event})


class EventUpdateView(UpdateView):
    model = Event
    template_name = 'plataforma/event/event_update.html'
    fields = ['name', 'data', 'address']
    success_url = '/'


class EventDeleteView(DeleteView):
    model = Event
    template_name = 'plataforma/event/event_delete.html'
    success_url = '/'


class EventDetailView(DetailView):
    model = Event
    template_name = 'plataforma/event/event_detail.html'
    context_object_name = 'event'


class EventListView(LoginRequiredMixin, ListView):
    model = Event
    template_name = 'plataforma/event/event_list.html'
    context_object_name = 'events'
    paginate_by = 2

    def get_queryset(self):
        queryset = super().get_queryset()
        query = self.request.GET.get('q')
        if query:
            queryset = queryset.filter(title__icontains=query)
            print(queryset.query)
        orderby = self.request.GET.get('pub_date', 'name')
        return queryset.order_by(orderby)
