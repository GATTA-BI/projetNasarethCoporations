# Generated by Django 4.2.9 on 2024-02-01 23:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inscription', '0005_alter_inscription_cv'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='inscription',
            name='image_diplome',
        ),
        migrations.AddField(
            model_name='inscription',
            name='diplome',
            field=models.FileField(blank=True, null=True, upload_to='documents'),
        ),
    ]
