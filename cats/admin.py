from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from . models import Cats, Adoption
from django import forms


class CatsAdmin(admin.ModelAdmin):
    list_display = (
        'pk',
        'name',
        'date_born',
        'gender',
        'description',
        'image',
        'status',
        'adopt_status',
        'date_created',
    )

    ordering = ('name',)

    
admin.site.register(Cats, CatsAdmin)
admin.site.register(Adoption)