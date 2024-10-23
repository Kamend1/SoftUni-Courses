from django.core.validators import MinValueValidator
from django.db import models
from WorldOfSpeedAppExamPrep24022024.profiles.validators import CustomMinLengthValidator, CustomRegexValidator


# Create your models here.
class Profile(models.Model):
    username = models.CharField(
        max_length=15,
        validators=[
            CustomMinLengthValidator(2),
            CustomRegexValidator(),
        ],
        blank=False,
        null=False,
    )

    email = models.EmailField(blank=False, null=False)

    age = models.PositiveIntegerField(
        MinValueValidator(21),
        blank=False,
        null=False,
    )

    password = models.CharField(max_length=20, blank=False, null=False)

    first_name = models.CharField(max_length=25, blank=True, null=True)

    last_name = models.CharField(max_length=25, blank=True, null=True)

    profile_picture = models.URLField(blank=True, null=True)
