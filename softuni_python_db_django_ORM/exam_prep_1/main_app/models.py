from django.core.validators import MinLengthValidator, MaxLengthValidator, MinValueValidator, MaxValueValidator
from django.db import models
from main_app.mixins import IsAwarded, LastUpdated
from main_app.custom_managers import DirectorManager


# Create your models here.
class BaseMovieEmployee(models.Model):
    full_name = models.CharField(
        max_length=120,
        validators=[
            MinLengthValidator(2),
        ],
    )

    birth_date = models.DateField(default='1900-01-01')

    nationality = models.CharField(max_length=50, default='Unknown')

    class Meta:
        abstract = True


class Director(BaseMovieEmployee):
    years_of_experience = models.SmallIntegerField(
        default=0,
        validators=[MinValueValidator(0)]
    )

    objects = DirectorManager()


class Actor(LastUpdated, IsAwarded, BaseMovieEmployee):
    pass


class MovieGenreChoices(models.TextChoices):
    ACTION = 'Action', 'Action'
    COMEDY = 'Comedy', 'Comedy'
    DRAMA = 'Drama', 'Drama'
    OTHER = 'Other', 'Other'


class Movie(LastUpdated, IsAwarded):
    title = models.CharField(
        max_length=150,
        validators=[MinLengthValidator(5)])

    release_date = models.DateField()

    storyline = models.TextField(null=True, blank=True)

    genre = models.CharField(
        max_length=6,
        choices=MovieGenreChoices.choices,
        default=MovieGenreChoices.OTHER,
    )

    rating = models.DecimalField(
        max_digits=3,
        decimal_places=1,
        validators=[MinValueValidator(0.0), MaxValueValidator(10.0)],
        default=0.0,
    )

    is_classic = models.BooleanField(default=False)

    director = models.ForeignKey(Director,
                                 on_delete=models.CASCADE,
                                 related_name='director_movies')
    starring_actor = models.ForeignKey(Actor,
                                       on_delete=models.SET_NULL,
                                       related_name='starring_movies',
                                       null=True, blank=True)
    actors = models.ManyToManyField(Actor,
                                    related_name='actor_movies')

