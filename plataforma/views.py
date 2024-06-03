from django.shortcuts import render

from .models import Chat, Event, Post, Story


def home(request):
    story = Story.objects.all()
    post = Post.objects.all()
    event = Event.objects.all()
    chat = Chat.objects.all()

    return render(request, 'home.html', {'story': story, 'post': post, 'event': event, 'chat': chat})
