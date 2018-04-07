from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.views.decorators.http import require_GET, require_http_methods

from qa.forms import AskForm, AnswerForm
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


@require_http_methods(["GET", "POST"])
def qa_question(request, id=None):
    question = get_object_or_404(Question, pk=id)

    if request.method == 'POST':
        form = AnswerForm(request.POST)
        if form.is_valid():
            answer = form.save(question)
            return HttpResponseRedirect(answer.question.get_url())
    else:
        form = AnswerForm(request.POST)

    return render(request, 'qa/question.html',
        {'question': question, 'form': form})


@require_http_methods(["GET", "POST"])
def ask(request):
    if request.method == 'POST':
        form = AskForm(request.POST)
        if form.is_valid():
            question = form.save()
            return HttpResponseRedirect(question.get_url())
    else:
        form = AskForm()

    return render(request, 'qa/ask.html', {'form': form})
