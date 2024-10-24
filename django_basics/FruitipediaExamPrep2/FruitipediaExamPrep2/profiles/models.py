from django.core.exceptions import ValidationError
from django.core.validators import MinLengthValidator
from django.db import models
from FruitipediaExamPrep2.profiles.validators import FirstLetterValidator, CustomLengthValidator


# Create your models here.
class Profile(models.Model):
    first_name = models.CharField(
        max_length=25,
        validators=[
            MinLengthValidator(2),
            FirstLetterValidator(),
        ],
        blank=False,
        null=False,
    )

    last_name = models.CharField(
        max_length=35,
        validators=[
            MinLengthValidator(1),
            FirstLetterValidator(),
        ],
        blank=False,
        null=False,
    )

    email = models.EmailField(unique=True, max_length=40, blank=False, null=False)

    password = models.CharField(
        max_length=20,
        validators=[CustomLengthValidator(),],
        blank=False,
        null=False,
        error_messages={
            'max_length': "*Password length requirements: 8 to 20 characters",
        },
    )

    image_url = models.URLField(blank=True, null=True)

    age = models.PositiveIntegerField(null=True, blank=True, default=18)
