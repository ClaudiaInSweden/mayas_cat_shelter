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
            'full_name': forms.TextInput(attrs={'placeholder': 'Full Name *'}),
            'email': forms.TextInput(attrs={'placeholder': 'E-Mail *'}),
            'phone': forms.TextInput(attrs={'placeholder': 'Please enter your phone number incl. country code *'}), 
            'date_of_birth': forms.DateInput(attrs={'placeholder': 'Select date...','type': 'date', 'max': datetime.now().date()}),
            'about_you': forms.Textarea(attrs={'placeholder': 'Please tell us about you, your family and your experience with cats *'}),
        }
    def __init__(self, *args, **kwargs):
        """
        Set autofocus on full_name field and remove auto-labels
        """
        super().__init__(*args, **kwargs)
        self.fields['full_name'].widget.attrs['autofocus'] = True
        for field in self.fields:
            self.fields[field].label = False


