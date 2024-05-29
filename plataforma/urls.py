from django.urls import path

from .class_views.post import Postcreateview, Postlistview, Postdetailview, Postupdateview, Postdeleteview

from .views import home

URLSPOSTS = [
    path('posts/create', Postcreateview.as_view(), name='post-create'),
    path('posts/', Postlistview.as_view(), name='post-list'),
    path('posts/<int:pk>/', Postdetailview.as_view(), name='post-detail'),
    path('posts/<int:pk>/update', Postupdateview.as_view(), name='post-update'),
    path('posts/<int:pk>/delete', Postdeleteview.as_view(), name='post-delete'),
]

urlpatterns = [
    path('', home, name='home')
] + URLSPOSTS
