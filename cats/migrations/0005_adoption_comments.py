# Generated by Django 4.2 on 2024-03-20 12:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cats', '0004_alter_adoption_options_adoption_status_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='adoption',
            name='comments',
            field=models.TextField(blank=True, null=True),
        ),
    ]