from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


STATUS = ((0, "Draft"), (1, "Published"))
GENDER = ((0, "male"), (1, "female"))


class Cats(models.Model):
    cat_id = models.AutoField(primary_key=True)
    catname = models.CharField(max_length=20)
    born = models.DateField()
    gender = models.IntegerField(choices=GENDER, default=0)
    description = models.TextField(blank=True)
    image = CloudinaryField('image', default='placeholder')
    status = models.IntegerField(choices=STATUS, default=0)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="cat_id"
    )



