from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.


class User(AbstractUser):
    name = models.CharField(max_length=150, default='')
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=150, default='')
    description = models.CharField(max_length=500, default='')

    def __str__(self):
        return self.name


class Partner(models.Model):
    name = models.CharField(max_length=150, default='')
    description = models.CharField(max_length=500)

class Company(models.Model):
    name = models.CharField(max_length=150)
    description = models.CharField(max_length=500)
    def __str__(self):
        return f"{self.name} ({self.description})"