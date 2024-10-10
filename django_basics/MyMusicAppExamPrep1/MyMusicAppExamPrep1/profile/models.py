from django.core.validators import MinValueValidator, MinLengthValidator
from MyMusicAppExamPrep1.profile.validators import UserNameValidator
from django.db import models


# Create your models here.
class Profile(models.Model):
    username = models.CharField(
        max_length=15,
        validators=[
            MinLengthValidator(2),
            UserNameValidator(),
        ],
    )

    email = models.EmailField(
        blank=False,
        null=False,
    )

    age = models.IntegerField(
        validators=[
            MinValueValidator(0),
        ],
    )
