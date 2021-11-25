from django.db import models


class Person(models.Model):
    name = models.CharField(max_length=200)
    country = models.CharField(max_length=200)
    age = models.PositiveIntegerField()


class Meta:
    ordering = ['id']


class Family(models.Model):
    name = models.CharField(max_length=100)
    members = models.IntegerField()
# Create your models here.
