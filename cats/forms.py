from django.forms import ModelForm
from django import forms
from datetime import datetime
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError
from phonenumber_field.formfields import PhoneNumberField
from phonenumber_field.widgets import PhoneNumberPrefixWidget
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout
from crispy_forms import bootstrap, layout
from .models import Cats, Adoption


class DateInput(forms.DateInput):
    input_type = 'date'


class CatsForm(ModelForm):
    class Meta:
        model = Cats
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'date_born': forms.TextInput(attrs={'class': 'form-control'}),
            'gender': forms.Select(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 5}),
            'status': forms.Select(attrs={'class': 'form-control'}),
            'adopt_status': forms.Select(attrs={'class': 'form-control'}),
        }


class AdoptionForm(ModelForm):
    class Meta:
        model = Adoption
        fields = ('full_name', 'email', 'phone', 'date_of_birth', 'about_you', 'cats',)
        widgets = {
            'full_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Full Name *'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'E-Mail *'}),
            'phone': PhoneNumberPrefixWidget(attrs={'placeholder': ('Phone number'), 'class': 'form-control'}, initial='SE'), 
            'date_of_birth': forms.DateInput(attrs={'class': 'form-control', 'placeholder': 'Select date...','type': 'date', 'max': datetime.now().date()}),
            'about_you': forms.Textarea(attrs={'class': 'form-control', 'rows': 5, 'placeholder': 'Please tell us about you, your family and your experience with cats *'}),
        }
       
    def __init__(self, *args, **kwargs):
        """
        Set autofocus on full_name field and remove auto-labels
        """
        super().__init__(*args, **kwargs)
        self.fields['full_name'].widget.attrs['autofocus'] = True
        for field in self.fields:
            self.fields[field].label = False



class StatusForm(ModelForm):
    class Meta:
        model = Adoption
        fields = ('full_name', 'email', 'phone', 'date_of_birth', 'about_you', 'cats', 'status', 'comments',)

        widgets = {
            'full_name': forms.TextInput(attrs={'class': 'form-control', 'readonly': 'readonly'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'readonly': 'readonly'}),
            'phone': PhoneNumberPrefixWidget(attrs={'readonly': 'readonly'}), 
            'date_of_birth': forms.DateInput(attrs={'readonly': 'readonly'}),
            'about_you': forms.Textarea(attrs={'readonly': 'readonly'}),
            'status': forms.Select(attrs={'class': 'form-control'}),
            'comments': forms.Textarea(attrs={'class': 'form-control', 'rows': 5, 'placeholder': 'Comments'}),
        }
       
    def __init__(self, *args, **kwargs):
        """
        Set autofocus on full_name field and remove auto-labels
        """
        super().__init__(*args, **kwargs)
        self.fields['status'].widget.attrs['autofocus'] = True
        for field in self.fields:
            self.fields[field].label = False