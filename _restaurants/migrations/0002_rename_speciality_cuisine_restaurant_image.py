# Generated by Django 4.2 on 2023-04-08 09:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('_restaurants', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Speciality',
            new_name='Cuisine',
        ),
        migrations.AddField(
            model_name='restaurant',
            name='image',
            field=models.ImageField(default=None, upload_to='images/'),
        ),
    ]
