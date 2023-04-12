from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    context = {}
    return render(request, 'blogtemplate.html', context)

def detail(request, question_id):
    return HttpResponse("Essa é a página da questão %s." % question_id)

def results(request, question_id):
    response = ("Essa é a página da  resultados %s.")
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("Essa é uma página de votação da questão %s. " %question_id)
