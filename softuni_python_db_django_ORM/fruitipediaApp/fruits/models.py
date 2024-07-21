from django.db import models


# Create your models here.
class Fruits(models.Model):
    name = models.CharField(null=False, blank=False, unique=True)