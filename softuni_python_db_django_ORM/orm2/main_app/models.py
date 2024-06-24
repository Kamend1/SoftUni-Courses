from datetime import date

from django.db import models


# Create your models here.
class Employee(models.Model):
    name = models.CharField(max_length=30)
    email_address = models.EmailField()
    photo = models.URLField()
    birth_date = models.DateField()
    works_full_time = models.BooleanField()
    created_on = models.DateTimeField(auto_now_add=True)


class Department(models.Model):
    class CityChoices(models.TextChoices):
        SOFIA = "Sofia"
        PLOVDIV = "Plovdiv"
        BURGAS = "Burgas"
        VARNA = "Varna"

    code = models.CharField(
        max_length=4,
        primary_key=True,
        unique=True
    )

    name = models.CharField(
        max_length=50,
        unique=True
    )

    employees_count = models.PositiveIntegerField(
        default=1,
        verbose_name="Employees Count"
    )

    location = models.CharField(
        max_length=20,
        choices=CityChoices.choices,
        null=True,
        blank=True
    )

    last_edited_on = models.DateTimeField(
        auto_now=True,
        editable=False
    )


class Project(models.Model):
    name = models.CharField(
        max_length=100,
        unique=True
    )

    description = models.TextField(
        null=True,
        blank=True
    )

    budget = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        null=True,
        blank=True
    )

    duration_in_days = models.PositiveIntegerField(
        null=True,
        blank=True,
        verbose_name="Duration in Days"
    )

    estimated_hours = models.FloatField(
        null=True,
        blank=True,
        verbose_name="Estimated Hours"
    )

    start_date = models.DateField(
        null=True,
        blank=True,
        verbose_name="Start Date",
        default=date.today()
    )

    created_on = models.DateTimeField(
        auto_now_add=True,
        editable=False
    )

    last_edited_on = models.DateTimeField(
        auto_now=True,
        editable=False
    )


class Person(models.Model):
    name = models.CharField(max_length=30)
    age = models.PositiveIntegerField()


class Blog(models.Model):
    post = models.TextField()
    author = models.CharField(max_length=35)


class WeatherForecast(models.Model):
    date = models.DateField()
    temperature = models.FloatField()
    humidity = models.FloatField()
    precipitation = models.FloatField()


class Recipe(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField()
    ingredients = models.TextField()
    cook_time = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)


class Product(models.Model):
    name = models.CharField(max_length=70)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)


class UserProfile(models.Model):
    username = models.CharField(max_length=65, unique=True)
    first_name = models.CharField(max_length=40, null=True)
    last_name = models.CharField(max_length=40, null=True)
    email = models.EmailField(default="students@softuni.bg", unique=True)
    bio = models.TextField(max_length=120)
    profile_image_url = models.URLField()
    created_at = models.DateTimeField(auto_now_add=True)


class Exercise(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    difficulty_level = models.CharField(max_length=20)
    duration_minutes = models.PositiveIntegerField()
    equipment = models.CharField(max_length=90)
    video_url = models.URLField(null=True, blank=True)
    calories_burned = models.PositiveIntegerField(default=1)
    is_favorite = models.BooleanField(default=False)


class Book(models.Model):
    class GenreChoices(models.TextChoices):
        FICTION = "Fiction"
        NONFICTION = "Non-Fiction"
        SCIENCEFICTION = "Science Fiction"
        HORROR = "Horror"

    title = models.CharField(max_length=30)
    author = models.CharField(max_length=100)
    genre = models.CharField(max_length=20, choices=GenreChoices.choices)
    publication_date = models.DateField(auto_now_add=True, editable=False)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    is_available = models.BooleanField(default=True)
    rating = models.FloatField()
    description = models.TextField()

    def __str__(self):
        return self.title
