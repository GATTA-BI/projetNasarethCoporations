# Generated by Django 4.2.9 on 2024-02-20 12:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inscription', '0028_alter_inscription_date_naissance'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inscription',
            name='image_profil',
            field=models.FileField(blank=True, upload_to='photos'),
        ),
    ]
