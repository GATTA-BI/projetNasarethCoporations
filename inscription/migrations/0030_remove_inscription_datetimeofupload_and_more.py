# Generated by Django 4.2.9 on 2024-02-20 13:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inscription', '0029_alter_inscription_image_profil'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='inscription',
            name='dateTimeOfUpload',
        ),
        migrations.AlterField(
            model_name='inscription',
            name='image_profil',
            field=models.ImageField(blank=True, upload_to='photos'),
        ),
    ]
