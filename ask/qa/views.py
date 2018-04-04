from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404

from qa.models import Question

def placeholder(request, *args, **kwargs):
    return HttpResponse('placeholder page')

def qa_home(request):
    questions = Question.objects.new()
    return render(request, 'qa/home.html', {'questions': questions,})

def qa_popular(request):
    questions = Question.objects.popular()
    return render(request, 'qa/home.html', {'questions': questions,})

def qa_question(request, id=None):
    question = get_object_or_404(Question, pk=id)
    return render(request, 'qa/detail.html', {'question': question,})
