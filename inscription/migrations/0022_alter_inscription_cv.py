# Generated by Django 4.2.9 on 2024-02-05 22:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inscription', '0021_remove_inscription_diplome_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inscription',
            name='cv',
            field=models.ImageField(blank=True, null=True, upload_to='images'),
        ),
    ]