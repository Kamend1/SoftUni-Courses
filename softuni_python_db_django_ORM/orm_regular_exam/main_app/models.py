from django.core.validators import RegexValidator, MinValueValidator
from django.db import models
from main_app.mixins import NameMixin, UpdatedAtMixin, LaunchDateMixin
from main_app.custom_managers import AstronautCustomManager


# Create your models here.
class Astronaut(NameMixin, UpdatedAtMixin):

    phone_number = models.CharField(
        max_length=15,
        unique=True,
        validators=[RegexValidator(regex=r'^[0:9]+')]
    )

    is_active = models.BooleanField(default=True)

    date_of_birth = models.DateField(null=True, blank=True)

    spacewalks = models.IntegerField(
        validators=[MinValueValidator(0)],
        default=0
    )

    objects = AstronautCustomManager()

    def __str__(self):
        return self.name

class Spacecraft(NameMixin, UpdatedAtMixin, LaunchDateMixin):

    manufacturer = models.CharField(max_length=100)

    capacity = models.SmallIntegerField(validators=[MinValueValidator(1)])

    weight = models.FloatField(validators=[MinValueValidator(0.0)])

    def __str__(self):
        return self.name


class MissionStatusChoices(models.TextChoices):
    PLANNED = "Planned", "Planned"
    ONGOING = "Ongoing", "Ongoing"
    COMPLETED = "Completed", "Completed"


class Mission(NameMixin, UpdatedAtMixin, LaunchDateMixin):

    description = models.TextField(null=True, blank=True)

    status = models.CharField(
        max_length=9,
        choices=MissionStatusChoices.choices,
        default=MissionStatusChoices.PLANNED,
    )

    spacecraft = models.ForeignKey('Spacecraft', on_delete=models.CASCADE, related_name='missions')

    astronauts = models.ManyToManyField('Astronaut', related_name='missions_astronauts')

    commander = models.ForeignKey(
        'Astronaut',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='mission_commander',
    )

    def __str__(self):
        return self.name
