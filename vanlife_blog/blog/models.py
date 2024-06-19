from django.db import models
from django.contrib.auth.models import User
from django.conf import settings  # This is required for the ForeignKey to the user model
from django.utils import timezone


class Journey(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    start_date = models.CharField(max_length=100)  #i changed those to char_field. remember to mrntion it in readme.dm
    end_date = models.CharField(max_length=100)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    participants = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='joined_journeys', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='posts')
    title = models.CharField(max_length=200)
    content = models.TextField()
    # objects=models.Manager() # turns out i dont need this here because django mysteriously takes care of it
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
    location = models.CharField(max_length=200, blank=True, null=True)
    likes = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='liked_posts', blank=True)
    def publish(self):
        self.published_date = timezone.now()
        self.save()
    def __str__(self):
        return self.title


class Comment(models.Model):
    post =models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    author= models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    text=models.TextField()
    created_date=models.DateTimeField(default=timezone.now)
    approved =models.BooleanField(default=True)

    def __str__(self):
        return f'Comment by {self.author} on {self.post}'


