from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


class Train(models.Model):
    Train_Name = models.CharField(max_length=25)
    Train_Type = models.CharField(max_length=25)
    Source = models.CharField(max_length=20)
    Destination = models.CharField(max_length=20)
    Travel_Time = models.CharField(max_length=15)
    General_Class = models.CharField(max_length=15)
    First_Class = models.CharField(max_length=15)

    def __str__(self):
        return self.Train_Name


    def get_absolute_url(self):
        return reverse('train-detail', kwargs={'pk': self.pk})