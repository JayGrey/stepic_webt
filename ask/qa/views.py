from django.shortcuts import render
from django.http import HttpResponse


def placeholder(request, *args, **kwargs):
    return HttpResponse('OK')

def qa_home(request):
    return HttpResponse('home page')

def qa_popular(request):
    return HttpResponse('popular page')

def qa_question(request, id=None):
    if id is None:
        raise Http404("qestion is not set")

    return HttpResponse('question page: ' + id)
