from django.conf import settings
from django.db import models
from django.utils import timezone


class Registration(models.Model):
    firstName = models.CharField(max_length=200)
    lastName = models.CharField(max_length=200)


    def publish(self):
        self.save()

    def __str__(self):
        return self.lastName