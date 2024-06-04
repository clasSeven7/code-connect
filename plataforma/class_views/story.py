from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import (CreateView, DeleteView, DetailView, ListView,
                                  UpdateView)

from plataforma.forms import StoryForm
from plataforma.models import Story


class StoryCreateView(CreateView):
    model = Story
    template_name = 'plataforma/story/story_create.html'
    fields = ['name', 'image']
    success_url = '/'

    def get(self, request):
        form_story = StoryForm()
        return render(request, 'plataforma/story/story_create.html', {'form_story': form_story})


class StoryUpdateView(UpdateView):
    model = Story
    template_name = 'plataforma/story/story_update.html'
    fields = ['name', 'image']
    success_url = '/'


class StoryDeleteView(DeleteView):
    model = Story
    template_name = 'plataforma/story/story_delete.html'
    success_url = '/'


class StoryDetailView(DetailView):
    model = Story
    template_name = 'plataforma/story/story_detail.html'
    context_object_name = 'story'


class StoryListView(LoginRequiredMixin, ListView):
    model = Story
    template_name = 'plataforma/story/story_list.html'
    context_object_name = 'storys'
    paginate_by = 2

    def get_queryset(self):
        queryset = super().get_queryset()
        query = self.request.GET.get('q')
        if query:
            queryset = queryset.filter(title__icontains=query)
            print(queryset.query)
        orderby = self.request.GET.get('pub_date', 'name')
        return queryset.order_by(orderby)
