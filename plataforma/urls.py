from django.urls import path

from .class_views.chat import (ChatCreateView, ChatDeleteView, ChatDetailView,
                               ChatListView, ChatUpdateView)
from .class_views.event import (EventCreateView, EventDeleteView,
                                EventDetailView, EventListView,
                                EventUpdateView)
from .class_views.post import (PostCreateView, PostDeleteView, PostDetailView,
                               PostListView, PostUpdateView)
from .class_views.story import (StoryCreateView, StoryDeleteView,
                                StoryDetailView, StoryListView,
                                StoryUpdateView)
from .views import home

URLSPOSTS = [
    path('posts/', PostListView.as_view(), name='post_list'),
    path('posts/create', PostCreateView.as_view(), name='post_create'),
    path('posts/<int:pk>/', PostDetailView.as_view(), name='post_detail'),
    path('posts/<int:pk>/update', PostUpdateView.as_view(), name='post_update'),
    path('posts/<int:pk>/delete', PostDeleteView.as_view(), name='post_delete'),
]

URLSCHAT = [
    path('chats/', ChatListView.as_view(), name='chat_list'),
    path('chats/create', ChatCreateView.as_view(), name='chat_create'),
    path('chats/<int:pk>/', ChatDetailView.as_view(), name='chat_detail'),
    path('chats/<int:pk>/update', ChatUpdateView.as_view(), name='chat_update'),
    path('chats/<int:pk>/delete', ChatDeleteView.as_view(), name='chat_delete'),
]

URLSEVENTS = [
    path('events/', EventListView.as_view(), name='event_list'),
    path('events/create', EventCreateView.as_view(), name='event_create'),
    path('events/<int:pk>/', EventDetailView.as_view(), name='event_detail'),
    path('events/<int:pk>/update', EventUpdateView.as_view(), name='event_update'),
    path('events/<int:pk>/delete', EventDeleteView.as_view(), name='event_delete'),
]

URLSSTORY = [
    path('stories/', StoryListView.as_view(), name='story_list'),
    path('stories/create', StoryCreateView.as_view(), name='story_create'),
    path('stories/<int:pk>/', StoryDetailView.as_view(), name='story_detail'),
    path('stories/<int:pk>/update', StoryUpdateView.as_view(), name='story_update'),
    path('stories/<int:pk>/delete', StoryDeleteView.as_view(), name='story_delete'),
]


urlpatterns = [
    path('', home, name='home')
] + URLSPOSTS + URLSCHAT + URLSEVENTS + URLSSTORY
