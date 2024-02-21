# Generated by Django 4.2.9 on 2024-02-01 21:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Inscription',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=200, null=True)),
                ('fonction', models.CharField(choices=[('Professeur', 'Professeur'), ('Professeure', 'Professeure'), ('Educatrice', 'Educatrice'), ('Educateur', 'Educateur')], max_length=200, null=True)),
                ('telephone', models.CharField(max_length=200, null=True)),
            ],
        ),
    ]