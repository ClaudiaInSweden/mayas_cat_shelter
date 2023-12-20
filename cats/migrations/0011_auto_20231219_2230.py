# Generated by Django 3.2.23 on 2023-12-19 22:30

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cats', '0010_auto_20231219_1730'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cats',
            name='featured_image',
        ),
        migrations.AddField(
            model_name='cats',
            name='image',
            field=cloudinary.models.CloudinaryField(default='placeholder', max_length=255, verbose_name='image'),
        ),
    ]