from django.shortcuts import render, redirect, get_object_or_404
from django.views import generic, View
from django.http import HttpResponse
from .models import Cats



def home(request):
    return render(request, "index.html")


class Cats(View):
    def cat_list(request):
        queryset = Cats.objects.filter(status=1)
        cat_detail = get_object_or_404(queryset)

        class Meta:
            ordering = ["catname"]

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



def adoption(request):
    return render(request, "adoption.html")