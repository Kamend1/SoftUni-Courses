from django.core.validators import MinLengthValidator
from django.db import models
from MyPlantAppExamPrep3.profiles.validators import FirstCapitalLetterValidator


# Create your models here.
class Profile(models.Model):
    username = models.CharField(
        max_length=10,
        validators=[MinLengthValidator(2),],
        blank=False,
        null=False,
    )

    first_name = models.CharField(
        max_length=20,
        validators=[FirstCapitalLetterValidator(),],
        blank=False,
        null=False,
    )

    last_name = models.CharField(
        max_length=20,
        validators=[FirstCapitalLetterValidator(), ],
        blank=False,
        null=False,
    )

    profile_picture = models.URLField(blank=True, null=True)
