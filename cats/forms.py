from django.forms import ModelForm
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from phone_field import PhoneField
from .models import Cats, Adoption


class CatsForm(ModelForm):
    class Meta:
        model = Cats
        fields = '__all__'
        exclude = ('author',)


class UserForm(UserCreationForm):
    first_name = forms.CharField()
    last_name = forms.CharField()
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'email', 'password1' ,'password2')


class AdoptionForm(ModelForm):
    class Meta:
        model = Adoption
        fields = ('phone', 'date_of_birth', 'about_you')
       
