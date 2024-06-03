from django.db import models


class Story(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to='images/', blank=True, null=True)

    def __str__(self):
        return self.name


class Post(models.Model):
    icon_user = models.ImageField(upload_to='images/', blank=True, null=True)
    name = models.CharField(max_length=50)
    data = models.DateField()
    hour = models.TimeField()
    content = models.TextField()
    image_post = models.ImageField(upload_to='images/', blank=True, null=True)

    def __str__(self):
        return self.name


class Event(models.Model):
    name = models.CharField(max_length=50)
    data = models.DateField()
    address = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Chat(models.Model):
    name = models.CharField(max_length=50)
    icon_user = models.ImageField(upload_to='images/', blank=True, null=True)

    def __str__(self):
        return self.name
