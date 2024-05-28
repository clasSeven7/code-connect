from django.http import HttpResponse
from django.views.generic import (CreateView, DeleteView, DetailView, ListView,
                                  UpdateView)

from plataforma.models import Story


class StoryCreateView(CreateView):
    model = Story
    template_name = 'story/story_create.html'
    fields = ['name', 'image']
    success_url = '/'

class StoryUpdateView(UpdateView):
    model = Story
    template_name = 'story/story_update.html'
    fields = ['name', 'image']
    success_url = '/'

class StoryDeleteView(DeleteView):
    model = Story
    template_name = 'story/story_delete.html'
    success_url = '/'

class StoryDetailView(DetailView):
    model = Story
    template_name = 'story/story_detail.html'
    context_object_name = 'story'

class StoryListView(ListView):
    model = Story
    template_name = 'story/story_list.html'
    context_object_name = 'storys'