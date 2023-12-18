from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Cats, Application
from .forms import CatsForm


def cats(request):
    cats = Cats.objects.filter(status=1)
    context = {'cats': cats}
    return render(request, 'cats.html', context)


def createCat(request):
    form = CatsForm()

    if request.method == 'POST':
        form = CatsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('cats')

    context = {'form': form}
    return render(request, 'admin_cat.html', context)


def updateCat(request, id):
    cat = Cats.objects.get(id=id)
    form = CatsForm(instance=cat)

    if request.method == 'POST':
        form = CatsForm(request.POST, instance=cat)
        if form.is_valid():
            form.save()
            return redirect('cats')

    context = {'form': form}
    return render(request, 'admin_cat.html', context)


def deleteCat(request, id):
    cat = Cats.objects.get(id=id)

    if request.method == 'POST':
        cat.delete()
        return redirect('cats')
    return render(request, 'messages.html', {'item': cat})


def application(request):
    application = Application.objects.all()
    context = {'application': application}
    return render(request, 'application.html', context)


def home(request):
    return render(request, 'index.html')