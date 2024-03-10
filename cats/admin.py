from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from . models import Cats, Adoption
from django import forms
from phonenumber_field.widgets import PhoneNumberPrefixWidget


class CatsAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'born',
        'gender',
        'description',
        'image',
        'status',
        'adopt_status',
        'date_created',
    )

    ordering = ('name',)


class AdoptionAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'email',
        'phone',
        'date_of_birth',
        'about_you',
        'date_created',
        'catname',
    )

admin.site.register(Cats, CatsAdmin)
admin.site.register(Adoption, AdoptionAdmin)