from django.shortcuts import render
from django.http import HttpResponse
from .models import Question

# Create your views here.
def index(request):
    question = Question.objects.get(id=1)
    return HttpResponse(question.question_text)

def detail(request, question_id):
    question = Question.objects.get(id=question_id)
    return HttpResponse("You're looking at question: %s" % question.question_text)

def results(request, question_id):
    return HttpResponse("You're looking for results for question %s" % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s" % question_id)