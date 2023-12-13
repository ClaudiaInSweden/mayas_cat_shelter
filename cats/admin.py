from django.contrib import admin
from .models import Cats
from django_summernote.admin import SummernoteModelAdmin

admin.site.register(Cats)

# Register your models here.
