# Generated by Django 3.1 on 2020-09-07 03:35

import cloudinary.models
import django.core.validators
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0005_post_liked'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=cloudinary.models.CloudinaryField(blank=True, max_length=255, validators=[django.core.validators.FileExtensionValidator(['png', 'jpeg', 'jpg', 'MP4', 'AVI*', 'MP3'])], verbose_name='posts'),
        ),
    ]