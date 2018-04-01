from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User


class QuestionManager(models.Manager):
    def new(self):
        return self.order_by('-added_at')

    def popular(self):
        return self.order_by('-likes')


class Question(models.Model):
    title = models.CharField(max_length = 32)
    text = models.TextField()
    added_at = models.DateField()
    rating = models.IntegerField()
    author = models.ForeignKey(User)
    likes = models.ManyToManyField(User, related_name='likes')

    def __str__(self):
        return 'Question (title={}, text={}, added_at={}, rating={})'.format(
            self.title, self.text, self.added_at, self.rating)


class Answer(models.Model):
    text = models.TextField()
    added_at = models.DateField(auto_now_add = True)
    question = models.ForeignKey(Question)
    author = models.ForeignKey(User)

    def __str__(self):
        return 'Answer (text={}, added_at={})'.format(self.text, self.added_at)
