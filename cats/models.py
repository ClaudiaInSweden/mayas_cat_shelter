from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from django_resized import ResizedImageField
from phone_field import PhoneField

class Cats(models.Model):

    class Meta:
        verbose_name_plural = 'Cat'

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


    name = models.CharField(max_length=200, null=False, blank=False)
    born = models.DateField(null=True, blank=True)
    gender = models.CharField(choices=GENDER, default='Male')
    description = models.TextField(null=True, blank=True)
    image = CloudinaryField('image', default='placeholder')
    status = models.CharField(choices=STATUS, default='Draft')
    adopt_status = models.CharField(choices=ADOPT_STATUS, default='Ready for adoption')
    date_created = models.DateField(auto_now_add=True)
   

    class Meta:
        ordering = ['name']

    def __str__(self):
        return f'{self.name} - Identification nr.: {self.id}'
    

class Adoption(models.Model):

    full_name = models.CharField(max_length=200, null=False, blank=False)
    email = models.EmailField(null=False, blank=False)
    phone = PhoneField(null=False, blank=False)
    date_of_birth = models.DateField(null=False, blank=False)
    about_you = models.TextField(null=False, blank=False)
    cats = models.ManyToManyField(Cats)
    received = models.DateField(auto_now_add=True)
   
   
    def __str__(self):
        return f'{self.full_name}'