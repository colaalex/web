from django.http import HttpResponse
from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404

from .models import Question, Answer


def test(request, *args, **kwargs):
    return HttpResponse('OK')


def new_questions(request):
    questions = Question.objects.new()
    page = request.GET.get('page', 1)
    paginator = Paginator(questions, 10)
    paginator.baseurl = '/?page='
    page = paginator.page(page)
    return render(request, 'questions_list.html', {
        'questions': page.object_list,
        'paginator': paginator,
        'page': page,
    })


def popular_questions(request):
    questions = Question.objects.popular()
    page = request.GET.get('page', 1)
    paginator = Paginator(questions, 10)
    paginator.baseurl = '/popular/?page='
    page = paginator.page(page)
    return render(request, 'questions_list.html', {
        'questions': page.object_list,
        'paginator': paginator,
        'page': page,
    })


def question_details(request, id):
    question = get_object_or_404(Question, id=id)
    answers = Answer.objects.filter(question=id)
    return render(request, 'question_details.html', {
        'question': question,
        'answers': answers,
    })
