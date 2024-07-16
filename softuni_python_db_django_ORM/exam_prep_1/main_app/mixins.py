from django.core.validators import MinLengthValidator, MaxLengthValidator, MinValueValidator
from django.db import models


class LastUpdated(models.Model):
    last_updated = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class IsAwarded(models.Model):
    is_awarded = models.BooleanField(default=False)

    class Meta:
        abstract = True
