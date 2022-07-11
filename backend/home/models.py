from django.conf import settings
from django.db import models


class Timert(models.Model):
    "Generated Model"
    name23 = models.TextField()


class Rite(models.Model):
    "Generated Model"
    username = models.TextField()
    address = models.TextField(
        null=True,
        blank=True,
    )
    company = models.TextField(
        null=True,
        blank=True,
    )
