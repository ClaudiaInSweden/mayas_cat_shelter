# Generated by Django 3.2.23 on 2023-12-17 23:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cats', '0005_auto_20231217_2358'),
    ]

    operations = [
        migrations.AlterField(
            model_name='application',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
