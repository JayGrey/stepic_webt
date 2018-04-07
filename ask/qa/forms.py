from django import forms
from django.contrib.auth.models import User

from qa.models import Question, Answer

class AskForm(forms.Form):
    title = forms.CharField(label = 'Title', max_length=32)
    text = forms.CharField(label = 'Text', widget=forms.Textarea)

    def save(self):
        # user = User.objects.get(pk=1)
        params = {
            'title':self.cleaned_data['title'],
            'text': self.cleaned_data['text'],
            # 'author': user
        }

        return Question.objects.create(**params)


class AnswerForm(forms.Form):
    text = forms.CharField(label = 'Text', widget=forms.Textarea)
    question = forms.IntegerField(widget=forms.HiddenInput())

    def clean_question(self):
        q_id = int(self.cleaned_data['question'])
        try:
            question = Question.objects.get(pk=q_id)
        except Question.DoesNotExist, Question.MultipleObjectsReturned:
            raise forms.ValidationError("wrong question id")

        return q_id

    def save(self, question):
        # user = User.objects.get(pk=1)
        question = Question.objects.get(pk=self.cleaned_data['question'])

        params = {
            'text': self.cleaned_data['text'],
            'question': question,
            # 'author': user
        }

        return Answer.objects.create(**params)
