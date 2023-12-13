from django.shortcuts import render, get_object_or_404
from django.views.generic.base import RedirectView
from django.views import generic, View
from django.http import HttpResponseRedirect
from .models import Cats



def home(request):
    return render(request, "index.html")


class Cats(View):
    def get(self, request):
        queryset = Cats.objects.filter(status=1)
        cats = get_object_or_404(queryset, catname=catname)

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
