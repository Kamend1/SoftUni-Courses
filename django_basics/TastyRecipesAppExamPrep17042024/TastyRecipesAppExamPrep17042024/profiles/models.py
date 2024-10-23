from django.db import models
from TastyRecipesAppExamPrep17042024.profiles.validators import CustomMinLengthValidator, FirstLetterCapitalValidator


# Create your models here.
class Profile(models.Model):
    nickname = models.CharField(
        max_length=20,
        validators=[
            CustomMinLengthValidator(2),
        ],
        unique=True,
        blank=False,
        null=False,
    )

    first_name = models.CharField(
        max_length=30,
        validators=[
            FirstLetterCapitalValidator()
        ],
        blank=False,
        null=False,
    )

    last_name = models.CharField(
        max_length=30,
        validators=[
            FirstLetterCapitalValidator()
        ],
        blank=False,
        null=False,
    )

    chef = models.BooleanField(
        blank=False,
        null=False,
        default=False,
    )

    bio = models.TextField()