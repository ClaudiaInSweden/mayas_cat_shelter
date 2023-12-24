from django.forms import ModelForm
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from phone_field import PhoneField
from .models import Cats, Adoption


class DateInput(forms.DateInput):
    input_type = 'date'


class CatsForm(ModelForm):
    class Meta:
        model = Cats
        fields = '__all__'
        exclude = ('author', 'selected',)
        widgets = {
            'catname': forms.TextInput(attrs={'class': 'form-control'}),
            'born': DateInput(),
            'gender': forms.Select(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'author': forms.TextInput(attrs={'class': 'form-control'}),
            'selected': forms.Select(attrs={'class': 'form-control'}),
        }


class AdoptionForm(ModelForm):
    class Meta:
        model = Adoption
        fields = '__all__'
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.TextInput(attrs={'class': 'form-control'}),
            'phone': forms.TextInput(attrs={'class': 'form-control'}),
            'date_of_birth': DateInput(),
            'about_you': forms.Textarea(attrs={'class': 'form-control'}),
            'selected': forms.Select(attrs={'class': 'form-control'}),
        }
       
