from django import forms
from django.forms import ModelForm
from .models import Application




class Application(forms.Form):
    class Meta:
        model = Application
        fields = ('first_name', 'last_name', 'email', 'date_of_birth', 'about_you',)
        
        
        
        