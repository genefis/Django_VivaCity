# Generated by Django 5.0.1 on 2024-01-17 06:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('VivaCityApp', '0002_galleryimage'),
    ]

    operations = [
        migrations.AddField(
            model_name='galleryimage',
            name='aos_delay',
            field=models.IntegerField(default=150),
        ),
    ]
