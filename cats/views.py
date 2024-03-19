from django.shortcuts import render, redirect, get_object_or_404, reverse
from django.views.decorators.csrf import csrf_protect 
from django import forms
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from cloudinary.forms import cl_init_js_callbacks
from .models import Cats, Adoption
from .forms import CatsForm, AdoptionForm


def cats(request):
    cats = Cats.objects.filter(status='Published')
    context = {'cats': cats}
    return render(request, 'cats.html', context)


def createCat(request):
    form = CatsForm()
    form_class = CatsForm

    if request.method == 'POST':
        form = CatsForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'The cat has been added to the list of cats!')
            return redirect('administration')
        else:
            messages.error(request, 'Your form could not be submitted. Please make sure the form is valid.')
            form = createCat()

    context = {'form': form}
    return render(request, 'admin_cat.html', context)


def updateCat(request, pk):
    cat = get_object_or_404(Cats, id=pk)
    form = CatsForm(instance=cat)

    if request.method == 'POST':
        form = CatsForm(request.POST, request.FILES, instance=cat)
        if form.is_valid():
            form.save()
            messages.info(request, 'The cat was updated successfully!')
            return redirect('administration')
        else:
            form = updateCat()

    context = {'form': form}
    return render(request, 'admin_cat.html', context)


def deleteCat(request, pk):
    cat = Cats.objects.get(id=pk)
    if request.method == 'POST':
        cat.delete()
        return redirect('administration')
    context = {'cat': cat}
    return render(request, 'delete.html', context)


def adoption(request):
    form = AdoptionForm()
    
    if request.method == 'POST':
        form = AdoptionForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your adoption request has been submitted successfully!')
            return redirect('home')
        else:
            messages.error(request, 'Your form could not be submitted. Please make sure the form is valid.')
            form = AdoptionForm()

    context = {'form': form}
    return render(request, 'adoption.html', context)


def home(request):
    return render(request, 'index.html')


def rules(request):
    return render(request, 'adoption_rules.html')


def administration(request):
    catlist = Cats.objects.all()
    context = {'catlist': catlist}
    return render(request, 'administration.html', context)