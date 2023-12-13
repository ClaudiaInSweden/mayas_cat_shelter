from django.db import models
from cloudinary.models import CloudinaryField


STATUS = ((0, "Draft"), (1, "Published"))
GENDER = ((0, "male"), (1, "female"))


class Cats(models.Model):
    id = models.IntegerField(primary_key=True, unique=True)
    catname = models.CharField(max_length=20)
    born = models.DateField()
    gender = models.IntegerField(choices=GENDER, default=0)
    description = models.TextField(blank=True)
    image = CloudinaryField('image', default='placeholder')
    status = models.IntegerField(choices=STATUS, default=0)

    class Meta:
        db_table = "Cats"




# Create your models here.
