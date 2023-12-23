from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from . models import Cats, Adoption
from django import forms
from phonenumber_field.widgets import PhoneNumberPrefixWidget

admin.site.register(Cats)
admin.site.register(Adoption)

