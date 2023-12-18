from django.db import models


class Cats(models.Model):

    STATUS = ((0, "Draft"), (1, "Published"))
    GENDER = ((0, "male"), (1, "female"))

    id = models.AutoField(primary_key=True)
    catname = models.CharField(max_length=50)
    born = models.DateField(null=True, blank=True)
    gender = models.IntegerField(choices=GENDER, default=0)
    description = models.TextField(null=True, blank=True)
    # featured_image = CloudinaryField('image', default='placeholder')
    # author = User
    status = models.IntegerField(choices=STATUS, default=0)

    def __str__(self):
        return self.catname


class Application(models.Model):
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=100, null=False, blank=False)
    last_name = models.CharField(max_length=100, null=False, blank=False)
    email = models.EmailField(null=False, blank=False)
    phone = models.IntegerField(null=False, blank=False)
    date_of_birth = models.DateField(null=False, blank=False)
    about_you = models.TextField(null=False, blank=False)

    def __str__(self):
        return self.last_name

