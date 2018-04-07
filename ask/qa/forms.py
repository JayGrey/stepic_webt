from django import forms
from django.contrib.auth.models import User

from qa.models import Question

class AskForm(forms.Form):
    title = forms.CharField(label = 'Title', max_length=32)
    text = forms.CharField(label = 'Text', widget=forms.Textarea)

    def save(self):
        user = User.objects.get(pk=1)
        params = {
            'title':self.cleaned_data['title'],
            'text': self.cleaned_data['text'],
            'author': user
        }

        return Question.objects.create(**params)


class AnswerForm(forms.Form):
    text = forms.CharField(label = 'Text', widget=forms.Textarea)
