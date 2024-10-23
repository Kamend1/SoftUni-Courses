from django.core.exceptions import ValidationError
from django.core.validators import MinLengthValidator, MinValueValidator
from django.db import models, IntegrityError
from django.db.models import Q


# Create your models here.
class CuisineTypeChoices(models.TextChoices):
    FRENCH = "French", "French"
    CHINESE = "Chinese", "Chinese"
    ITALIAN = "Italian", "Italian"
    BALKAN = "Balkan", "Balkan"
    OTHER = "Other", "Other"


class Recipe(models.Model):
    title = models.CharField(
        max_length=100,
        validators=[
            MinLengthValidator(10),
        ],
        unique=True,
        null=False,
        blank=False,
    )

    cuisine_type = models.CharField(
        max_length=7,
        choices=CuisineTypeChoices.choices,
        null=False,
        blank=False,
    )

    ingredients = models.TextField(
        null=False,
        blank=False,
        help_text="Ingredients must be separated by a comma and space.",
    )

    instructions = models.TextField(
        null=False,
        blank=False,
    )

    cooking_time = models.PositiveIntegerField(
        validators=[MinValueValidator(1),],
        help_text="Provide the cooking time in minutes.",
        null=False,
        blank=False,
    )

    image_url = models.URLField(
        null=True,
        blank=True,
    )

    author = models.ForeignKey(
        to='profiles.Profile',
        on_delete=models.CASCADE,
    )

    def clean(self):
        if Recipe.objects.filter(Q(title=self.title)).exists():
            raise ValidationError({'title': 'We already have a recipe with the same title!'})

    def save(self, *args, **kwargs):
        self.clean()
        super().save(*args, **kwargs)
