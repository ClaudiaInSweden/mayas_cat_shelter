from django.forms import ModelForm
from django import forms
from datetime import date
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError
from phonenumber_field.formfields import PhoneNumberField
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
    def clean_date_of_birth(self):
       data = self.cleaned_data['date_of_birth']
       age = (date.today() - data).days / 365
       if age < 19:
         raise forms.ValidationError('You must be at least 19 years old to adopt a cat!')
       return data 

    class Meta:
        model = Adoption
        fields = ('full_name', 'email', 'phone', 'date_of_birth', 'about_you', 'cats',)
        widgets = {
            'full_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Full Name *'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'E-Mail *'}),
            'phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Phone number *, use format +46 123456789'}), 
            'date_of_birth': forms.DateInput(attrs={'type': 'date'}),
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


    # def clean_renewal_date(self):
    #     data = self.cleaned_data['date_of_birth']

    #     # Check if a date is not in the past.
    #     if data < datetime.date.today() + datetime.timedelta(years=19):
    #         raise ValidationError(_('Minimum age for adopting a cat is 19!'))

    #     # Check if a date is in the allowed range (+4 weeks from today).
    #     if data > datetime.date.today() + datetime.timedelta(years=70):
    #         raise ValidationError(_('Maximum age for adopting a cat is 70!'))

    #     # Remember to always return the cleaned data.
    #     return data


class StatusForm(ModelForm):
    class Meta:
        model = Adoption
        fields = ('full_name', 'email', 'phone', 'date_of_birth', 'about_you', 'cats', 'status', 'comments',)

        widgets = {
            'full_name': forms.TextInput(attrs={'class': 'form-control', 'readonly': 'readonly'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'readonly': 'readonly'}),
            'phone': forms.TextInput(attrs={'readonly': 'readonly'}), 
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