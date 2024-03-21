# Generated by Django 4.2 on 2024-03-20 12:23

from django.db import migrations, models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('cats', '0003_alter_adoption_phone'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='adoption',
            options={'ordering': ['-received']},
        ),
        migrations.AddField(
            model_name='adoption',
            name='status',
            field=models.CharField(choices=[('New Request', 'New Request'), ('Contacted', 'Contacted'), ('Home Visit', 'Home Visit'), ('Booked', 'Booked'), ('Adopted', 'Adopted')], default='New Request'),
        ),
        migrations.AlterField(
            model_name='adoption',
            name='phone',
            field=phonenumber_field.modelfields.PhoneNumberField(default='Phone number *', max_length=128, region=None),
        ),
        migrations.AlterField(
            model_name='cats',
            name='born',
            field=models.DateField(blank=True, default='Will be updated soon', null=True),
        ),
        migrations.AlterField(
            model_name='cats',
            name='description',
            field=models.TextField(blank=True, default='Will be updated soon', null=True),
        ),
    ]