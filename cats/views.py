from django.shortcuts import render, redirect, get_object_or_404, reverse
from django.views import generic, View
from django.http import HttpResponseRedirect
from django import forms
from .models import Cats, Application
from bootstrap_datepicker_plus.widgets import DateTimePickerInput



def home(request):
    return render(request, "index.html")


class Catsview(View):
    def get(self, request, *args):
        queryset = Cats.objects.filter(status=1)
        ourcats = get_object_or_404(queryset)

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

class ApplicationForm(forms.ModelForm):

    class Meta:
        model = Application
        fields = '__all__'

    def application(request):
        form = Application()
        return render(request, 'application.html', {'form': form})



    # def get_form(self):
    #     form = get_form(Application)
    #     form.fields['date_of_birth'].widget = DateTimePickerInput()

    # def application(request):
    #     submitted = False
    #     if request.method == 'POST':
    #         form = Application(request.POST)
    #         if form.is_valid():
    #             form.save()
    #             return HttpResponseRedirect('/application?submitted=True')
    #     else:
    #         form = Application
    #     if 'submitted' in request.GET:
    #         submitted = True

        # return render(request, 'application.html', {'form': form, 'submitted': submitted})



def Adoption(request):
    return render(request, 'adoption.html')