# Generated by Django 4.2.9 on 2024-02-05 23:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inscription', '0022_alter_inscription_cv'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='inscription',
            name='cv',
        ),
    ]