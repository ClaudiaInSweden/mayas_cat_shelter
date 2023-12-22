from django.db import models
from cloudinary.models import CloudinaryField


class Cats(models.Model):

    STATUS = ((0, "Draft"), (1, "Published"))
    GENDER = ((0, "male"), (1, "female"))

    id = models.AutoField(primary_key=True)
    catname = models.CharField(max_length=50)
    born = models.DateField(null=True, blank=True)
    gender = models.IntegerField(choices=GENDER, default=0)
    description = models.TextField(null=True, blank=True)
    image = CloudinaryField('image', default='https://res.cloudinary.com/dhciyvwx5/image/upload/v1703206863/default_aivdfc.png')
    # author = User
    status = models.IntegerField(choices=STATUS, default=0)

    def __str__(self):
        return self.catname

    # @property
    # def imageURL(self):      
    #     try:
    #         img = self.image.url
    #     except:
    #         img = ''
    #     return img


class Application(models.Model):
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=100, null=False, blank=False)
    last_name = models.CharField(max_length=100, null=False, blank=False)
    email = models.EmailField(null=False, blank=False)
    phone = models.IntegerField(null=False, blank=False)
    date_of_birth = models.DateField(null=False, blank=False)
    about_you = models.TextField(null=False, blank=False)
    cat_id = models.ForeignKey(Cats, on_delete=models.DO_NOTHING, null=True, blank=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'