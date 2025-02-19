from django.db import models
from rest_framework import serializers
from django.contrib.auth.models import User



class Attendant(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=200)
    discord = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15)
    crew = models.CharField(max_length=100)
    ticketCrewID = models.CharField(max_length=100, null=True)
    profile_image = models.ImageField(upload_to='profile_images/', blank=True, null=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

# Create your models here.
