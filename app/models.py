from turtle import ondrag
from django.contrib.auth.models import User
from django.db import models
from django.db.models.base import Model

# Create your models here.


class todo(models.Model):
    date_created = models.DateTimeField(null=False)
    content = models.CharField(max_length=200)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, null=True, blank=True)
    description = models.CharField(max_length=400, null=True,)


class register(models.Model):
    username = models.CharField(max_length=200, null=False)
    email = models.CharField(max_length=200, null=False)
    password = models.CharField(max_length=200, null=False)
