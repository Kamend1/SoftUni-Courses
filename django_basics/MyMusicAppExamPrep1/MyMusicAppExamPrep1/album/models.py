from django.core.validators import MinValueValidator
from django.db import models

from MyMusicAppExamPrep1.profile.models import Profile


# Create your models here.
class GenreChoices(models.TextChoices):
    POP = "Pop Music", "Pop Music"
    JAZZ = "Jazz Music", "Jazz Music"
    RNB = "R&B Music", "R&B Music"
    ROCK = "Rock Music", "Rock Music"
    COUNTRY = "Country Music", "Country Music"
    DANCE = "Dance Music", "Dance Music"
    HIP_HOP = "Hip Hop Music", "Hip Hop Music"
    OTHER = "Other", "Other"


class Album(models.Model):
    album_name = models.CharField(
        max_length=30,
        unique=True,
        blank=False,
        null=False,
    )

    artist = models.CharField(
        max_length=30,
        blank=False,
        null=False,
    )

    genre = models.CharField(
        max_length=30,
        choices=GenreChoices.choices,
        default=GenreChoices.OTHER,
        blank=False,
        null=False,
    )

    description = models.TextField(blank=True, null=True)

    image = models.URLField(
        blank=False,
        null=False,
    )

    price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        validators=[
            MinValueValidator(0.0),
        ]
    )

    #TODO lazy reference to Profile - Single Responsibility principle
    owner = models.ForeignKey(
        Profile,
        on_delete=models.CASCADE,

    )
