# Generated by Django 3.2.23 on 2023-12-22 01:02

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cats', '0012_alter_cats_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cats',
            name='image',
            field=cloudinary.models.CloudinaryField(default='https://res.cloudinary.com/dhciyvwx5/image/upload/v1703206863/default_aivdfc.png', max_length=255, verbose_name='image'),
        ),
    ]