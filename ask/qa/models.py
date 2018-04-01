from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone


class QuestionManager(models.Manager):
    def new(self):
        return self.order_by('-added_at')

    def popular(self):
        return self.order_by('-likes')


class Question(models.Model):
    title = models.CharField(max_length=32)
    text = models.TextField()
    added_at = models.DateField(default=timezone.now)
    rating = models.IntegerField(default=0)
    author = models.ForeignKey(User)
    likes = models.ManyToManyField(User, related_name='likes')

    def __str__(self):
        return '(title={}, text={}, added_at={}, rating={})'.format(
            self.title, self.text, self.added_at, self.rating)


class Answer(models.Model):
    text = models.TextField()
    added_at = models.DateField(default=timezone.now)
    question = models.ForeignKey(Question)
    author = models.ForeignKey(User)

    def __str__(self):
        return '(text={}, added_at={})'.format(self.text, self.added_at)
