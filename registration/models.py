from django.conf import settings
from django.db import models
from django.utils import timezone

BELT_CHOICES = (
	('white', 'White'),
	('yellow', 'Yellow'),
	('green', 'Green'),
	('brown', 'Brown'),
	('black', 'Black'),
)


class Registration(models.Model):
    firstName = models.CharField(max_length=50, verbose_name="First Name", blank=False, null=False)
    lastName = models.CharField(max_length=50, verbose_name="Last Name", blank=False, null=False)
    age = models.IntegerField(verbose_name="Age", blank=False, null=False)
    weight = models.IntegerField(verbose_name="Weight", help_text="Kilograms", blank=False, null=False)
    rank = models.CharField(max_length=6, choices=BELT_CHOICES, verbose_name="Belt Rank", blank=False, null=False)


    def publish(self):
        self.save()

    def __str__(self):
        return self.lastName