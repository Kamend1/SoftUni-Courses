from django.db import models


# Create your models here.
class Pet(models.Model):
    name = models.CharField(max_length=40)
    species = models.CharField(max_length=40)


class Artifact(models.Model):
    name = models.CharField(max_length=70)
    origin = models.CharField(max_length=70)
    age = models.PositiveIntegerField()
    description = models.TextField()
    is_magical = models.BooleanField(default=False)


class Location(models.Model):
    name = models.CharField(max_length=100)
    region = models.CharField(max_length=50)
    population = models.PositiveIntegerField()
    description = models.TextField()
    is_capital = models.BooleanField(default=False)


class Car(models.Model):
    model = models.CharField(max_length=40)
    year = models.PositiveIntegerField()
    color = models.CharField(max_length=40)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    price_with_discount = models.DecimalField(max_digits=10, decimal_places=2, default=0)


class Task(models.Model):
    title = models.CharField(max_length=25)
    description = models.TextField()
    due_date = models.DateField()
    is_finished = models.BooleanField(default=False)


class RoomTypeChoices(models.TextChoices):
    STANDARD = "St", "Standard"
    DELUXE = "D", "Deluxe"
    SUITE = "S", "Suite"


class HotelRoom(models.Model):
    room_number = models.PositiveIntegerField()
    room_type = models.CharField(max_length=10, choices=RoomTypeChoices.choices)
    capacity = models.PositiveIntegerField()
    amenities = models.TextField()
    price_per_night = models.DecimalField(max_digits=8, decimal_places=2)
    is_reserved = models.BooleanField(default=False)


class CharClassChoices(models.TextChoices):
    MAGE = "Mage", "Mage"
    WARRIOR = "Warrior", "Warrior"
    ASSASSIN = "Assassin", "Assassin"
    SCOUT = "Scout", "Scout"
    FUSION = "Fusion", "Fusion"


class Character(models.Model):
    name = models.CharField(max_length=100)
    class_name = models.CharField(max_length=20, choices=CharClassChoices.choices)
    level = models.PositiveIntegerField()
    strength = models.PositiveIntegerField()
    dexterity = models.PositiveIntegerField()
    intelligence = models.PositiveIntegerField()
    hit_points = models.PositiveIntegerField()
    inventory = models.TextField()
