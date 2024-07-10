from decimal import Decimal

from django.core.validators import MinValueValidator, EmailValidator, RegexValidator, URLValidator, MinLengthValidator
from django.db import models
from main_app.validators import validate_field_only_names_and_spaces


# Create your models here.
class Customer(models.Model):
    name = models.CharField(
        max_length=100,
        validators=[
            validate_field_only_names_and_spaces
        ]
    )

    age = models.PositiveIntegerField(
        validators=[
            MinValueValidator(
                18,
                message="Age must be greater than or equal to 18")
        ]
    )

    email = models.EmailField(error_messages={'invalid': 'Enter a valid email address'})

    phone_number = models.CharField(
        max_length=13,
        validators=[
            RegexValidator(
                regex=r"^\+359\d{9}$",
                message="Phone number must start with '+359' followed by 9 digits"
            )
        ]
    )

    website_url = models.URLField(error_messages={'invalid': 'Enter a valid URL'})


class BaseMedia(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    genre = models.CharField(max_length=50)
    created_at = models.DateField(auto_now_add=True)

    class Meta:
        abstract = True
        ordering = ['-created_at', 'title']


class Book(BaseMedia):
    author = models.CharField(
        max_length=100,
        validators=[MinLengthValidator(5, message='Author must be at least 5 characters long')]
    )

    isbn = models.CharField(
        max_length=20,
        unique=True,
        validators=[MinLengthValidator(6, message='ISBN must be at least 6 characters long')]
    )

    class Meta(BaseMedia.Meta):
        verbose_name = 'Model Book'
        verbose_name_plural = 'Models of type - Book'


class Movie(BaseMedia):
    director = models.CharField(
        max_length=100,
        validators=[MinLengthValidator(8, message='Director must be at least 8 characters long')]
    )

    class Meta(BaseMedia.Meta):
        verbose_name = 'Model Movie'
        verbose_name_plural = 'Models of type - Movie'


class Music(BaseMedia):
    artist = models.CharField(
        max_length=100,
        validators=[MinLengthValidator(9, message='Artist must be at least 9 characters long')]
    )

    class Meta(BaseMedia.Meta):
        verbose_name = 'Model Music'
        verbose_name_plural = 'Models of type - Music'


class Product(models.Model):
    TAX_RATE = 0.08
    PRICE_PER_WEIGHT_UNIT = 2.00

    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def calculate_tax(self) -> float:
        return float(self.price) * self.TAX_RATE

    def calculate_shipping_cost(self, weight: Decimal):
        return self.PRICE_PER_WEIGHT_UNIT * float(weight)

    def format_product_name(self):
        return f"Product: {self.name}"


class DiscountedProduct(Product):
    TAX_RATE = 0.05
    PRICE_PER_WEIGHT_UNIT = 1.50
    PRICE_FACTOR = 1.2

    class Meta:
        proxy = True

    def calculate_price_without_discount(self):
        return float(self.price) * self.PRICE_FACTOR

    def format_product_name(self):
        return f"Discounted Product: {self.name}"


class RechargeEnergyMixin(models.Model):

    class Meta:
        abstract = True

    def recharge_energy(self, amount: int):

        self.energy += amount

        if self.energy > 100:
            self.energy = 100

        self.save()


class Hero(RechargeEnergyMixin):
    name = models.CharField(max_length=100)
    hero_title = models.CharField(max_length=100)
    energy = models.PositiveIntegerField()


class SpiderHero(Hero):
    ENERGY_NEEDED_SWING = 80

    def swing_from_buildings(self):
        if self.energy < self.ENERGY_NEEDED_SWING:
            return f"{self.name} as Spider Hero is out of web shooter fluid"

        self.energy -= self.ENERGY_NEEDED_SWING

        if self.energy == 0:
            self.energy = 1

        self.save()
        return f"{self.name} as Spider Hero swings from buildings using web shooters"

    class Meta:
        proxy = True


class FlashHero(Hero):
    ENERGY_NEEDED_RUN_SUPERSPEED = 65

    def run_at_super_speed(self):
        if self.energy < self.ENERGY_NEEDED_RUN_SUPERSPEED:
            return f"{self.name} as Flash Hero needs to recharge the speed force"

        self.energy -= self.ENERGY_NEEDED_RUN_SUPERSPEED

        if self.energy == 0:
            self.energy = 1

        self.save()
        return f"{self.name} as Flash Hero runs at lightning speed, saving the day"

    class Meta:
        proxy = True
