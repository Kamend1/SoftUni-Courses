from django.db import models
from django.core.validators import MinLengthValidator, MinValueValidator, MaxValueValidator
from .mixins import IsAwardedMixin, LastUpdatedMixin
from .custom_manager import CustomDirectorManager


# Create your models here.
class BasePerson(models.Model):
    full_name = models.CharField(max_length=120,validators=[
        MinLengthValidator(2)])

    birth_date = models.DateField(default='1900-01-01')

    nationality = models.CharField(max_length=50, default='Unknown')

    class Meta:
        abstract = True


class Director(BasePerson):
    years_of_experience = models.SmallIntegerField(default=0, validators=[
        MinValueValidator(0)
    ])

    objects = CustomDirectorManager()

    def __str__(self):
        return self.full_name


class Actor(BasePerson, IsAwardedMixin, LastUpdatedMixin):
    pass

    def __str__(self):
        return self.full_name


class GenreMovieChoices(models.TextChoices):
    ACTION = 'Action', 'Action'
    COMEDY = 'Comedy', 'Comedy'
    DRAMA = 'Drama', 'Drama'
    OTHER = 'Other', 'Other'


class Movie(IsAwardedMixin, LastUpdatedMixin):
    title = models.CharField(max_length=150, validators=[
        MinLengthValidator(5)
    ])

    release_date = models.DateField()

    storyline = models.TextField(null=True, blank=True)

    genre = models.CharField(
        max_length=6,
        choices=GenreMovieChoices.choices,
        default=GenreMovieChoices.OTHER
    )

    rating = models.DecimalField(
        max_digits=3,
        decimal_places=1,
        default=0.0,
        validators=[
            MinValueValidator(0.0),
            MaxValueValidator(10.0)
        ]
    )

    is_classic = models.BooleanField(default=False)

    director = models.ForeignKey(Director, related_name='movies', on_delete=models.CASCADE)

    starring_actor = models.ForeignKey(
        Actor,
        related_name='starring_actor_movies',
        on_delete=models.SET_NULL,
        null=True
    )

    actors = models.ManyToManyField(Actor, related_name='movies_actors')

    def __str__(self):
        return self.title
