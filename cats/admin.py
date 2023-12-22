from django.contrib import admin

from django_summernote.admin import SummernoteModelAdmin

from . models import Cats, Adoption

admin.site.register(Cats)
admin.site.register(Adoption)