from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Cats, Application


def cats(request):
    queryset = Cats.objects.filter(status=1)
    return render(request, 'cats.html')

def application(request):
    application = Application.objects.all()
    return HttpResponse('This is our apply page')

def home(request):
    return render(request, 'index.html')