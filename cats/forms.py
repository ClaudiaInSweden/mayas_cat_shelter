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
            'name': forms.TextInput(attrs={'class': 'form-control',
                                           'aria-label': 'Cat name'}),
            'date_born': forms.TextInput(attrs={'class': 'form-control',
                                            'aria-label': 'Born'}),
            'gender': forms.Select(attrs={'class': 'form-control',
                                          'aria-label': 'Gender'}),
            'description': forms.Textarea(attrs={'class': 'form-control',
                                                'aria-label': 'Temperament',
                                          'rows': 5}),
            'status': forms.Select(attrs={'class': 'form-control',
                                          'aria-label': 'Publication status'}),
            'adopt_status': forms.Select(attrs={'class': 'form-control',
                                                'aria-label': 'Adopt status'}),
        }


class AdoptionForm(ModelForm):
    """
    Filter cats list so that only published cats are visible in the select box
    """
    cats = forms.ModelMultipleChoiceField(
        queryset=Cats.objects.filter(status='Published')
    )
    """
    Take cleaned data from birthday field and calculate 19 years back.
    Raise error if person is not at least 19 years old.
    """
    def clean_date_of_birth(self):
        data = self.cleaned_data['date_of_birth']
        age = (date.today() - data).days / 365
        if age < 19:
            raise forms.ValidationError('You must be at least 19 years old \
                                        to adopt a cat!')
        return data

    class Meta:
        model = Adoption
        fields = ('full_name', 'email', 'phone', 'date_of_birth', 'about_you',
                  'cats',)
        widgets = {
            'full_name': forms.TextInput(attrs={'class': 'form-control',
                                                'aria-label': 'Full Name',
                                                'placeholder': 'Full Name *'}),
            'email': forms.EmailInput(attrs={'class': 'form-control',
                                             'aria-label': 'E-Mail',
                                             'placeholder': 'E-Mail *'}),
            'phone': forms.TextInput(attrs={'class': 'form-control',
                                            'aria-label': 'Phone number',
                                            'placeholder': 'Phone number *, ' +
                                            'use format +46 123456789'}),
            'date_of_birth': forms.DateInput(attrs={'type': 'date',
                                                    'aria-label': 'Date of Birth'}),
            'about_you': forms.Textarea(attrs={'class': 'form-control',
                                               'aria-label': 'About you',
                                               'rows': 5, 'placeholder':
                                               'Please tell us about you, ' +
                                               'your family and your ' +
                                               'experience with cats *'}),
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
        fields = ('full_name', 'email', 'phone', 'date_of_birth', 'about_you',
                  'cats', 'status', 'comments',)
        """
        Load input data from adoption request but make them none-editable
        """
        widgets = {
            'full_name': forms.TextInput(attrs={'class': 'form-control',
                                                'readonly': 'readonly',
                                                'aria-label': 'Name'}),
            'email': forms.EmailInput(attrs={'class': 'form-control',
                                             'readonly': 'readonly',
                                             'aria-label': 'Email'}),
            'phone': forms.TextInput(attrs={'readonly': 'readonly',
                                            'aria-label': 'Phone'}),
            'date_of_birth': forms.DateInput(attrs={'readonly': 'readonly',
                                                    'aria-label': 'Born'}),
            'about_you': forms.Textarea(attrs={'readonly': 'readonly',
                                               'aria-label': 'About'}),
            'status': forms.Select(attrs={'class': 'form-control',
                                          'aria-label': 'Status'}),
            'comments': forms.Textarea(attrs={'class': 'form-control',
                                            'aria-label': 'Comments',
                                              'rows': 5,
                                              'placeholder': 'Comments'}),
        }

    def __init__(self, *args, **kwargs):
        """
        Set autofocus on full_name field and remove auto-labels
        """
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].label = False
