# Generated by Django 4.2.9 on 2024-02-01 22:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inscription', '0002_inscription_date_naissance_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='inscription',
            name='email',
            field=models.EmailField(max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='inscription',
            name='date_naissance',
            field=models.DateField(null=True),
        ),
    ]