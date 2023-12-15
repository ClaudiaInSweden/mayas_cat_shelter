from django.db import models
from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


STATUS = ((0, "Draft"), (1, "Published"))
GENDER = ((0, "male"), (1, "female"))




class Cats(models.Model):
    catname = models.CharField(max_length=20)
    born = models.DateField()
    gender = models.IntegerField(choices=GENDER, default=0)
    description = models.TextField(default='Will be updated soon!')
    image = CloudinaryField('image', default='placeholder')
    status = models.IntegerField(choices=STATUS, default=0)
    selected = models.BooleanField(default=False)

    class Meta:
        ordering = ['catname']


class ApplicationForm(models.Model):
    first_name = models.CharField(max_length=100, null=False, blank=False)
    last_name = models.CharField(max_length=100, null=False, blank=False)
    email = models.EmailField()
    phone = models.IntegerField()
    date_of_birth = models.DateTimeField()
    about_you = models.TextField(default='Please tell us something about you!')

    def __str__(self):
        return self.first_name









