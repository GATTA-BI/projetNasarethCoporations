# Generated by Django 4.2.9 on 2024-02-05 22:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inscription', '0020_inscription_cv_inscription_dernier_diplome_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='inscription',
            name='diplome',
        ),
        migrations.RemoveField(
            model_name='inscription',
            name='emploi_precedent',
        ),
        migrations.RemoveField(
            model_name='inscription',
            name='nombre_experience',
        ),
    ]
