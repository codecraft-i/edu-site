# Generated by Django 4.2 on 2024-01-03 20:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_alter_students_gender_alter_students_phone'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Students',
        ),
    ]
