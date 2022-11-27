from django.shortcuts import render, HttpResponse


def hello(request):
    return HttpResponse('hello')


def index(request):
    return render(request, 'index.html')
