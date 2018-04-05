from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
from django.views.decorators.http import require_GET

from qa.models import Question


def placeholder(request, *args, **kwargs):
    return HttpResponse('placeholder page')

@require_GET
def qa_home(request):

    if request.path == '/popular/':
        paginator = Paginator(Question.objects.popular(), 10)
    else:
        paginator = Paginator(Question.objects.new(), 10)

    try:
        questions = paginator.page(request.GET.get("page"))
    except PageNotAnInteger:
        questions = paginator.page(1)
    except EmptyPage:
        questions = paginator.page(paginator.num_pages)

    return render(request, 'qa/home.html',
        {'questions': questions, 'paginator': paginator})


@require_GET
def qa_question(request, id=None):
    question = get_object_or_404(Question, pk=id)
    return render(request, 'qa/detail.html', {'question': question,})
