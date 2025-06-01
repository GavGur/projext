from email.policy import default

from django.db import models

# Create your models here.

class Client(models.Model):
    login = models.CharField(max_length=200, default="")
    password = models.CharField(max_length=200, default="")


class Product(models.Model):
    title = models.CharField(max_length=200, default="")
    price = models.IntegerField(default=99)