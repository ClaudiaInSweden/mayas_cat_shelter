# Generated by Django 4.2.8 on 2023-12-23 14:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cats', '0015_adoption_alter_cats_image_delete_application_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cats',
            name='description',
            field=models.TextField(blank=True, default='placeholder', null=True),
        ),
        migrations.AlterField(
            model_name='cats',
            name='gender',
            field=models.CharField(choices=[('male', 'male'), ('female', 'female')], default='m'),
        ),
    ]