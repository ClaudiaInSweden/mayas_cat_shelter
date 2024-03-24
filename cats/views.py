from django.shortcuts import render, redirect, get_object_or_404, reverse
from django.views.decorators.csrf import csrf_protect 
from django import forms
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from cloudinary.forms import cl_init_js_callbacks

from django.contrib.auth.decorators import login_required
from .models import Cats, Adoption
from .forms import CatsForm, AdoptionForm, StatusForm


def cats(request):
    cats = Cats.objects.filter(status='Published')
    context = {'cats': cats}
    return render(request, 'cats.html', context)


@login_required
def createCat(request):
    if not request.user.is_superuser:
        messages.error(request, 'You are not authorized to perform this task!')
        return redirect(reverse('home'))
        
    form = CatsForm()

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


@login_required
def updateCat(request, pk):
    if not request.user.is_superuser:
        messages.error(request, 'You are not authorized to perform this task!')
        return redirect(reverse('home'))

    cat = get_object_or_404(Cats, id=pk)
    form = CatsForm(instance=cat)

    if request.method == 'POST':
        form = CatsForm(request.POST, request.FILES, instance=cat)
        if form.is_valid():
            form.save()
            messages.info(request, 'The cat was updated successfully!')
            return redirect('administration')
        else:
            messages.error(request, 'Your form could not be submitted. Please make sure the form is valid.')
            form = updateCat(instance=cat)

    context = {'form': form}
    return render(request, 'admin_cat.html', context)


@login_required
def deleteCat(request, pk):
    if not request.user.is_superuser:
        messages.error(request, 'You are not authorized to perform this task!')
        return redirect(reverse('home'))

    cat = Cats.objects.get(id=pk)
    if request.method == 'POST':
        cat.delete()
        messages.success(request, 'The cat has been deleted!')
        return redirect('administration')
    context = {'cat': cat}
    return render(request, 'delete.html', context)


def adoption(request):
    form = AdoptionForm()
    
    if request.method == 'POST':
        form = AdoptionForm(request.POST)
        if form.is_valid():
            adoption = form.save()
            messages.success(request, 'Your adoption request has been submitted successfully!')
            return redirect('home')
            
    else:
        form = AdoptionForm()

    context = {'form': form}
    return render(request, 'adoption.html', context)


@login_required
def updateStatus(request, pk):
    if not request.user.is_superuser:
        messages.error(request, 'You are not authorized to perform this task!')
        return redirect(reverse('home'))

    adoption = get_object_or_404(Adoption, id=pk)
    form = StatusForm(instance=adoption)

    if request.method == 'POST':
        form = StatusForm(request.POST, instance=adoption)
        if form.is_valid():
            adoption = form.save()
            messages.info(request, 'The adoption request was updated successfully!')
            return redirect('adopters-list')
        else:
            messages.error(request, 'The form could not be updated. Please make sure the form is valid.')
            form = StatusForm(instance=adoption)

    context = {'form': form}
    return render(request, 'admin_adoption.html', context)


def home(request):
    return render(request, 'index.html')


def rules(request):
    return render(request, 'adoption_rules.html')


@login_required
def administration(request):
    if not request.user.is_superuser:
        messages.error(request, 'You are not authorized to perform this task!')
        return redirect(reverse('home'))

    catlist = Cats.objects.all()
    context = {'catlist': catlist}
    return render(request, 'administration.html', context)


@login_required
def adoptersList(request):
    if not request.user.is_superuser:
        messages.error(request, 'You are not authorized to perform this task!')
        return redirect(reverse('home'))

    adoptionlist = Adoption.objects.all()
    context = {'adoptionlist': adoptionlist}
    return render(request, 'adoption_request.html', context)