from django.shortcuts import render
<<<<<<< HEAD

from .models import Chat, Event, Post, Story
=======
from .models import Chat, Event, Post, Story, User
>>>>>>> refs/remotes/origin/main

def home(request):
    story = Story.objects.all()
    post = Post.objects.all()
    event = Event.objects.all()
    chats = Chat.objects.all()

<<<<<<< HEAD
    return render(request, 'home.html', {'story': story, 'post': post, 'event': event, 'chat': chat})
=======
    return render(request, 'home.html', {'user': user, 'story': story, 'post': post, 'event': event, 'chats': chats})
>>>>>>> refs/remotes/origin/main
