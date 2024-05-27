from django.shortcuts import render

from .models import Chat, Event, Post, Story, User


def home(request):
    user = User.objects.all()
    story = Story.objects.all()
    post = Post.objects.all()
    event = Event.objects.all()
    chat = Chat.objects.all()

    return render(request, 'home.html', {'user': user, 'story': story, 'post': post, 'event': event, 'chat': chat})
