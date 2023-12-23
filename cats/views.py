from django.shortcuts import render, redirect, get_object_or_404, reverse
from django.views.decorators.csrf import csrf_protect 
from django import forms
from django.http import HttpResponse
from cloudinary.forms import cl_init_js_callbacks
from .models import Cats, Adoption
from .forms import CatsForm, AdoptionForm, UserForm


def cats(request):
    # cats = Cats.objects.filter(status=1)
    cats = Cats.objects.filter(status=1)
    context = {'cats': cats}
    return render(request, 'cats.html', context)

@csrf_protect 
def createCat(request):
    form = CatsForm()

    if request.method == 'POST':
        form = CatsForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('cats')

    context = {'form': form}
    return render(request, 'admin_cat.html', context)

@csrf_protect 
def updateCat(request, id):
    cat = Cats.objects.get(id=id)
    form = CatsForm(instance=cat)

    if request.method == 'POST':
        form = CatsForm(request.POST, request.FILES, instance=cat)
        if form.is_valid():
            form.save()
            return redirect('cats')

    context = {'form': form}
    return render(request, 'admin_cat.html', context)

@csrf_protect 
def deleteCat(request, id):
    cat = Cats.objects.get(id=id)

    if request.method == 'POST':
        cat.delete()
        return redirect('cats')
    return render(request, 'messages.html', {'item': cat})

@csrf_protect 
def adoption(request):
    if request.method == 'POST':
        form = AdoptionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('cats')
        else:
            form = AdoptionForm()
    context = {'adoption': adoption}
    return render(request, 'adoption.html', context)



def home(request):
    return render(request, 'index.html')