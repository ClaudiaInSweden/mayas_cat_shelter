from django.contrib import admin

from django_summernote.admin import SummernoteModelAdmin

from .models import Cats, Application

admin.site.register(Cats)
admin.site.register(Application)