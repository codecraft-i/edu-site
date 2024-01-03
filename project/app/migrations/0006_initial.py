# Generated by Django 4.2 on 2024-01-03 20:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('app', '0005_delete_students'),
    ]

    operations = [
        migrations.CreateModel(
            name='Students',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('telegram_username', models.CharField(max_length=50)),
                ('phone', models.CharField(max_length=15)),
                ('age', models.IntegerField()),
                ('gender', models.CharField(choices=[('male', 'Erkak'), ('female', 'Ayol')], max_length=6)),
                ('text', models.TextField()),
            ],
        ),
    ]
