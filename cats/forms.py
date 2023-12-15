from django import forms
from django.forms import ModelForm
from .models import ApplicationForm


class ApplicationForm(ModelForm):
    class Meta:
        model = ApplicationForm
        fields = ('__all__')
        