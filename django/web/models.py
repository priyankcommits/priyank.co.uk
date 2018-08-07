from datetime import datetime

from django.db import models
# Create your models here.


class Profile(models.Model):
    first_name = models.CharField(default='', max_length=200)
    last_name = models.CharField(default='', max_length=200)
    email = models.CharField(default='', max_length=200)
    image = models.CharField(default='', max_length=500)

    def str(self):
        return self.name


class Post(models.Model):
    by = models.ForeignKey(Profile, related_name='profile', on_delete=None)
    headline = models.CharField(default='', max_length=1000)
    subheadline = models.CharField(default='', max_length=1000)
    content = models.TextField(default='', max_length=100000)
    image = models.CharField(default='', max_length=500)
    likes = models.IntegerField(default=0)
    kind = models.IntegerField(default=0)
    upvote_value = models.IntegerField(default=0)
    downvote_value = models.IntegerField(default=0)
    upvote_label = models.CharField(default='Yes', max_length=200)
    downvote_label = models.CharField(default='No', max_length=200)
    created = models.DateTimeField(default=datetime.now)
    updated = models.DateTimeField(default=datetime.now)
    slug = models.SlugField(unique=False)

    def str(self):
        return self.headline


class Article(models.Model):
    headline = models.CharField(default='', max_length=200)
    text = models.CharField(default='', max_length=500)
    link = models.CharField(default='', max_length=1000)
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(default=datetime.now)
    updated = models.DateTimeField(default=datetime.now)

    def str(self):
        return self.headline


class Subscribers(models.Model):
    email = models.CharField(default='', max_length=300, unique=True)
    name = models.CharField(default='', max_length=100)

    def str(self):
        return self.email
