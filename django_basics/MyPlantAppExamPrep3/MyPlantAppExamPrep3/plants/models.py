from django.core.validators import MinLengthValidator
from django.db import models
from MyPlantAppExamPrep3.plants.validators import LetterValidator


# Create your models here.
class PlantTypeChoices(models.TextChoices):
    OUTDOOR_PLANTS = "Outdoor Plants", "Outdoor Plants"
    INDOOR_PLANTS = "Indoor Plants", "Indoor Plants"


class Plant(models.Model):
    type = models.CharField(
        max_length=14,
        blank=False,
        null=False,
        choices=PlantTypeChoices.choices,
    )

    name = models.CharField(
        max_length=20,
        validators=[
            MinLengthValidator(2),
            LetterValidator
        ],
        blank=False,
        null=False,
    )

    image_url = models.URLField(blank=False, null=False)

    description = models.TextField(blank=False, null=False)

    price = models.FloatField(blank=False, null=False)


