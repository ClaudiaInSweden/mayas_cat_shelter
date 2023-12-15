# Generated by Django 3.2.23 on 2023-12-15 12:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cats', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ApplicationForm',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.IntegerField()),
                ('date_of_birth', models.DateTimeField()),
                ('about_you', models.TextField(default='Please tell us something about you!')),
            ],
        ),
        migrations.AlterModelOptions(
            name='cats',
            options={'ordering': ['catname']},
        ),
        migrations.AddField(
            model_name='cats',
            name='selected',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='cats',
            name='description',
            field=models.TextField(default='Will be updated soon!'),
        ),
        migrations.AlterField(
            model_name='cats',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterModelTable(
            name='cats',
            table=None,
        ),
    ]
