from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from django_resized import ResizedImageField
from phone_field import PhoneField


class Cats(models.Model):

    STATUS = (
        ('Draft', 'Draft'),
        ('Published', 'Published')
    )
  
    GENDER = (
        ('Male', 'Male'),
        ('Female', 'Female')
    )

    ADOPT_STATUS = (
        ('Not yet ready for adoption', 'Not yet ready for adoption'),
        ('Ready for adoption', 'Ready for adoption'),
        ('Booked', 'Booked'),
        ('Adopted', 'Adopted')
    )


    name = models.CharField(max_length=200, null=True, blank=True)
    born = models.DateField(null=True, blank=True)
    gender = models.CharField(choices=GENDER, default='Male')
    description = models.TextField(null=True, blank=True)
    image = CloudinaryField('image', default='placeholder')
    status = models.CharField(choices=STATUS, default='Draft')
    adopt_status = models.CharField(choices=ADOPT_STATUS, default='Ready for adoption')
    date_created = models.DateField(auto_now_add=True, null=True)
   

    class Meta:
        ordering = ['name']

    def __str__(self):
        return f'{self.name} - {self.id}, - Born: {self.born}, - Status: {self.status} - Adoption status: {self.adopt_status}'
    

class Adoption(models.Model):


    name = models.CharField(max_length=200, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    phone = PhoneField(null=True, blank=True)
    date_of_birth = models.DateField(null=True, blank=True)
    about_you = models.TextField(null=True, blank=True)
    catname = models.ManyToManyField(Cats)
    date_created = models.DateField(auto_now_add=True, null=True)
   
   
    def __str__(self):
        return f'{self.name} Cat: {self.catname}'

