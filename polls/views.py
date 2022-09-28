from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
from .models import Question

# Create your views here.
def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:4]

    data = {
        'latest_question_list': latest_question_list
    }

    return render(request, 'polls/index.html', data)

def detail(request, question_id):
    # try:
    #     question = Question.objects.get(pk=question_id)
    # except Question.DoesNotExist:
    #     raise Http404("Question does not exist")
    question = get_object_or_404(Question, pk=question_id)
    
    return render(request, 'polls/detail.html', {
        'question': question
    })

def results(request, question_id):
    return HttpResponse("You're looking for results for question %s" % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s" % question_id)