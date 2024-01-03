# Generated by Django 4.2 on 2024-01-03 20:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='students',
            name='gender',
            field=models.CharField(choices=[('male', 'Erkak'), ('female', 'Ayol')], max_length=6),
        ),
        migrations.AlterField(
            model_name='students',
            name='phone',
            field=models.CharField(max_length=15),
        ),
    ]
