# Generated by Django 4.2.9 on 2024-02-21 00:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inscription', '0032_rename_image_profil_inscription_photo_profil'),
    ]

    operations = [
        migrations.AddField(
            model_name='inscription',
            name='date',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
