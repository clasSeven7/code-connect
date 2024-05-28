from django.http import HttpResponse
from django.views.generic import (CreateView, DeleteView, DetailView, ListView,
                                  UpdateView)


from plataforma.models import Event

class EventCreateView(CreateView):
    model = Event
    template_name = 'event/event_create.html'
    fields = ['name', 'data', 'address']
    success_url = '/'

class EventUpdateView(UpdateView):
    model = Event
    template_name = 'event/event_update.html'
    fields = ['name', 'data', 'address']
    success_url = '/'


class EventDeleteView(DeleteView):
    model = Event
    template_name = 'event/event_delete.html'
    success_url = '/'

class EventDetailView(DetailView):
    model = Event
    template_name = 'event/event_detail.html'
    context_object_name = 'event'


class EventListView(ListView):
    model = Event
    template_name = 'event/event_list.html'
    context_object_name = 'events'


