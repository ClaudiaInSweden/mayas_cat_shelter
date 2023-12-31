# Generated by Django 4.2.8 on 2023-12-22 18:51

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django_resized.forms


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('cats', '0013_alter_cats_image'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='cats',
            options={'ordering': ['catname']},
        ),
        migrations.AddField(
            model_name='cats',
            name='author',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='cats',
            name='catname',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='cats',
            name='description',
            field=models.TextField(blank=True, default='Will soon be updated.', null=True),
        ),
        migrations.AlterField(
            model_name='cats',
            name='gender',
            field=models.CharField(choices=[('m', 'male'), ('f', 'female')], default='m'),
        ),
        migrations.AlterField(
            model_name='cats',
            name='image',
            field=django_resized.forms.ResizedImageField(crop=None, default='CloudinaryImage("default_di3p4z.webp").image()', force_format='WEBP', help_text='Please upload images in landscape format', keep_meta=True, quality=75, scale=None, size=[300, 300], upload_to='projects/'),
        ),
    ]
