from django.shortcuts import render
from django.http import HttpResponse


def cats(request):
    return render(request, 'cats/cats.html')

def apply(request):
    return HttpResponse('This is our apply page')

def home(request):
    return render(request, 'cats/index.html')