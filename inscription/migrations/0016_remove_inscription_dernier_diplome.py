# Generated by Django 4.2.9 on 2024-02-05 20:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inscription', '0015_remove_inscription_cv_remove_inscription_email_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='inscription',
            name='dernier_diplome',
        ),
    ]
