from django.shortcuts import render
from django.http import HttpResponse

def req(request):
    HttpResponse('hello world!')

def information(request):
    sex = request.GET['sex']
    name = request.GET['name']
    response = 'You are ' + name + ' and of sex ' + sex
    HttpResponse(response)
# Create your views here.
