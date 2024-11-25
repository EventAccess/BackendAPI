from django.db import models
from rest_framework import serializers
from django.contrib.auth.models import User


# this is the Attendant model, im unsure if we need more data? Maby date of birth? => 18 years maby?
class Attendant(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(max_length=100)
    phone_number = models.CharField(max_length=12)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


# Create your models here.
