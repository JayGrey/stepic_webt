from django import forms
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User

from qa.models import Question, Answer


class AskForm(forms.Form):
    title = forms.CharField(label = 'Title', max_length=32)
    text = forms.CharField(label = 'Text', widget=forms.Textarea)

    def save(self, request):
        params = {
            'title':self.cleaned_data['title'],
            'text': self.cleaned_data['text'],
            'author': request.user,
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

    def clean(self):
        if not self._user.is_authenticated():
            raise forms.ValidationError("only authenticated users may leave answer")

    def save(self, question):
        # user = User.objects.get(pk=1)
        question = Question.objects.get(pk=self.cleaned_data['question'])

        params = {
            'text': self.cleaned_data['text'],
            'question': question,
            'author': self._user,
        }

        return Answer.objects.create(**params)

class SignupForm(forms.Form):
    username = forms.CharField(label = 'username')
    email = forms.EmailField()
    password = forms.CharField(label = 'password', widget=forms.PasswordInput)

    def clean_username(self):
        try:
            user = User.objects.get(username=self.cleaned_data['username'])
            raise forms.ValidationError("user already exists")
        except User.DoesNotExist:
            return self.cleaned_data['username']


    def save(self, request):
        params = {
            'username': self.cleaned_data['username'],
            'password': self.cleaned_data['password'],
            'email': self.cleaned_data['email'],
        }

        user =  User.objects.create_user(**params)
        login(request, user)

class LoginForm(forms.Form):
    username = forms.CharField(label = 'username')
    password = forms.CharField(label = 'password', widget=forms.PasswordInput)

    def clean(self):
        params = {
            'username': self.cleaned_data['username'],
            'password': self.cleaned_data['password'],
        }
        user = authenticate(**params)
        if user is None or not user.is_authenticated():
            raise forms.ValidationError('username or password is incorrect')

    def save(self, request):
        user = User.objects.get(username=self.cleaned_data['username'])
        login(request, user)
