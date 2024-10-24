from django.core.validators import MinLengthValidator
from django.db import models
from FruitipediaExamPrep2.fruits.validators import LetterValidator


# Create your models here.
class Fruit(models.Model):
    name = models.CharField(
        unique=True,
        max_length=30,
        validators=[
            MinLengthValidator(2),
            LetterValidator(),
        ],
        error_messages={
            'unique': "This fruit name is already in use! Try a new one.",
        },
        blank=False,
        null=False,
    )

    image_url = models.URLField(blank=False, null=False)

    description = models.TextField(blank=False, null=False)

    nutrition = models.TextField(blank=True, null=True)

    owner = models.ForeignKey(
        to='profiles.Profile',
        on_delete=models.CASCADE,
    )
