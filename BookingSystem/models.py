from django.db import models
from django.contrib.auth.models import User

class Customer(models.Model):
    First_Name = models.CharField(max_length=15)
    Last_Name = models.CharField(max_length=15)
    Age = models.IntegerField()
    Mobile = models.IntegerField()
    Email = models.CharField(max_length=50)
    Address = models.CharField(max_length=15)

