from django.db import models

# Create your models here.

from django.db import models

class Students(models.Model):
    name = models.CharField(max_length=100)
    telegram_username = models.CharField(max_length=50)
    phone = models.CharField(max_length=15)
    age = models.IntegerField()
    GENDER_CHOICES = [
        ('male', 'Erkak'),
        ('female', 'Ayol'),
    ]
    gender = models.CharField(max_length=6, choices=GENDER_CHOICES)
    text = models.TextField()