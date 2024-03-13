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
            return redirect('cats')
        else:
            form = createCat()

    context = {'form': form}
    return render(request, 'admin_cat.html', context)


def updateCat(request, pk):
    cat = Cats.objects.get(id=pk)
    form = CatsForm(instance=cat)

    if request.method == 'POST':
        form = CatsForm(request.POST, request.FILES, instance=cat)
        if form.is_valid():
            form.save()
            messages.success(request, 'The cat has been updated successfully!')
            return redirect('cats')
        else:
            form = updateCat()

    context = {'form': form}
    return render(request, 'admin_cat.html', context)


def deleteCat(request, pk):
    cat = Cats.objects.get(id=pk)
    if request.method == 'POST':
        cat.delete()
        return redirect('cats')
    context = {'cat': cat}
    return render(request, 'delete.html', context)


def adoption(request):
    adoption_form = AdoptionForm()
    
    if request.method == 'POST':
        adoption_form = AdoptionForm(request.POST)
        if adoption_form.is_valid():
            adoption_form.save()
            messages.success(request, 'Your adoption request has been submitted successfully!')
            return redirect('home')
        else:
            adoption_form = AdoptionForm()

    context = {
        'adoption_form': adoption_form,
        }
    return render(request, 'adoption.html', context)


def home(request):
    return render(request, 'index.html')


def rules(request):
    return render(request, 'adoption_rules.html')


def administration(request):
    catlist = Cats.objects.all()
    context = {'catlist': catlist}
    return render(request, 'administration.html', context)



