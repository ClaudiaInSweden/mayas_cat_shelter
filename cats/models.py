from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from django_resized import ResizedImageField
from phone_field import PhoneField


class Cats(models.Model):

    STATUS = [
        ('draft', 'draft'),
        ('published', 'published')
    ]
  
    GENDER = [
        ('male', 'male'),
        ('female', 'female')
    ]

    id = models.AutoField(primary_key=True)
    catname = models.CharField(max_length=100)
    born = models.DateField(null=True, blank=True)
    gender = models.CharField(choices=GENDER, default='m')
    description = models.TextField(null=True, blank=True)
    image = CloudinaryField('image', default='placeholder')
    author = models.ForeignKey(User, on_delete=models.DO_NOTHING, null=True, blank=True)
    status = models.IntegerField(choices=STATUS, default=0)
    selected = models.BooleanField(null=True, blank=True, default=False)

    class Meta:
        ordering = ['catname']

    def __str__(self):
        return f'{self.id} - {self.catname}, - Born: {self.born}, - Gender: {self.gender}, - Status: {self.status}'
    

class Adoption(models.Model):

    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=100, null=False, blank=False)
    last_name = models.CharField(max_length=100, null=False, blank=False)
    email = models.EmailField(null=False, blank=False)
    phone = PhoneField(null=True, blank=True)
    date_of_birth = models.DateField(null=False, blank=False)
    about_you = models.TextField(null=False, blank=False)
   
    def __str__(self):
        return f'{self.first_name} {self.last_name}, cat name and ID: {Cats.catname}, {Cats.id} '