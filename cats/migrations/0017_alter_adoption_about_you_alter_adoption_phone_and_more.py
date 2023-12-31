# Generated by Django 4.2.8 on 2023-12-23 15:43

from django.db import migrations, models
import phone_field.models


class Migration(migrations.Migration):

    dependencies = [
        ('cats', '0016_alter_cats_description_alter_cats_gender'),
    ]

    operations = [
        migrations.AlterField(
            model_name='adoption',
            name='about_you',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='adoption',
            name='phone',
            field=phone_field.models.PhoneField(blank=True, max_length=31, null=True),
        ),
        migrations.AlterField(
            model_name='cats',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
    ]
