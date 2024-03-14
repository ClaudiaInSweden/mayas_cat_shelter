from django.forms import ModelForm
from django import forms
from datetime import datetime
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from phonenumber_field.formfields import PhoneNumberField
from .models import Cats, Adoption


class DateInput(forms.DateInput):
    input_type = 'date'


class CatsForm(ModelForm):
    class Meta:
        model = Cats
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'born': forms.DateInput(attrs={'type': 'date', 'max': datetime.now().date()}),
            'gender': forms.Select(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'status': forms.Select(attrs={'class': 'form-control'}),
            'adopt_status': forms.Select(attrs={'class': 'form-control'}),
        }


class AdoptionForm(ModelForm):
    class Meta:
        model = Adoption
        fields = ('full_name', 'email', 'phone', 'date_of_birth', 'about_you', 'cats',)
        widgets = {
            'full_name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.TextInput(attrs={'class': 'form-control'}),
            # 'phone': forms.PhoneNumberField(attrs={'class': 'form-control'}),
            'date_of_birth': forms.DateInput(attrs={'type': 'date', 'max': datetime.now().date()}),
            'about_you': forms.Textarea(attrs={'class': 'form-control'}),
        }

