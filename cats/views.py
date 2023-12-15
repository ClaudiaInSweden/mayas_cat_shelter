from django.shortcuts import render, redirect, get_object_or_404, reverse
from django.views import generic, View
from django.http import HttpResponseRedirect
from .models import Cats
from .forms import ApplicationForm



def home(request):
    return render(request, "index.html")


class Cats(View):
    def catlist(self, request):
        queryset = Cats.objects.filter(status=1)

        return render(
            request,
            "cats.html",
            {
                "catname": catname,
                "born": born,
                "gender": gender,
                "description": description,
                "image": image
            }
        )

# Create your views here.

def application(request):
    submitted = False
    if request.method == 'POST':
        form = ApplicationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/application?submitted=True')
    else:
        form = ApplicationForm
    if 'submitted' in request.GET:
        submitted = True

    return render(request, 'application.html', {'form': form, 'submitted': submitted})



def adoption(request):
    return render(request, 'adoption.html')