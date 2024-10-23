from django.core.exceptions import ValidationError
from django.core.validators import MinLengthValidator, MinValueValidator
from django.db import models
from WorldOfSpeedAppExamPrep24022024.cars.validators import YearValidator


# Create your models here.
class CarTypeChoices(models.TextChoices):
    RALLY = "Rally", "Rally"
    OPEN_WHEEL = "Open-wheel", "Open Wheel"
    KART = "Kart", "Kart"
    DRAG = "Drag", "Drag"
    OTHER = "Other", "Other"


class Car(models.Model):
    type = models.CharField(
        max_length=10,
        choices=CarTypeChoices.choices,
        blank=False,
        null=False,
    )

    model = models.CharField(
        max_length=15,
        validators=[MinLengthValidator(1),],
        blank=False,
        null=False,
    )

    year = models.IntegerField(
        blank=False,
        null=False,
        validators=[YearValidator(),],
    )

    image_url = models.URLField(
        unique=True,
        null=False,
        blank=False,
    )

    price = models.FloatField(
        null=False,
        blank=False,
        validators=[MinValueValidator(1.0),],
    )

    owner = models.ForeignKey(
        to='profiles.Profile',
        on_delete=models.CASCADE,
    )

    def save(self, *args, **kwargs):
        try:
            super().save(*args, **kwargs)
        except ValidationError:
            raise ValidationError({'image_url': 'This image URL is already in use! Provide a new one.'})
