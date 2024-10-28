from django.core.validators import MinLengthValidator
from django.db import models
from FurryFunniesApp.authors.validators import LetterValidator, PassCodeValidator


# Create your models here.
class Author(models.Model):
    first_name = models.CharField(
        max_length=40,
        validators=[
            LetterValidator(),
            MinLengthValidator(4),
        ],
        blank=False,
        null=False,
    )

    last_name = models.CharField(
        max_length=40,
        validators=[
            LetterValidator(),
            MinLengthValidator(4),
        ],
        blank=False,
        null=False,
    )

    passcode = models.CharField(
        max_length=7,
        validators=[
            PassCodeValidator(6),
        ],
        blank=False,
        null=False,
    )

    pets_number = models.SmallIntegerField(blank=False, null=False)

    info = models.TextField(blank=True, null=True)

    image_url = models.URLField(blank=True, null=True)
