# Generated by Django 4.2 on 2023-04-08 19:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('_restaurants', '0006_cuisine_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cuisine',
            name='slug',
            field=models.SlugField(max_length=30, unique=True),
        ),
    ]
