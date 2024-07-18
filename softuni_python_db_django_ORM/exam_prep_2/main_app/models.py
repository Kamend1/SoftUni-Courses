from django.core.validators import MinLengthValidator, MinValueValidator
from django.db import models
from main_app.mixins import CreatedOnMixin
from main_app.managers import CustomProfileManager


# Create your models here.
class Profile(CreatedOnMixin):
    full_name = models.CharField(
        max_length=100,
        validators=[MinLengthValidator(2)]
    )

    email = models.EmailField()

    phone_number = models.CharField(max_length=15)

    address = models.TextField()

    is_active = models.BooleanField(default=True)

    objects = CustomProfileManager()

    def __str__(self):
        return f"{self.full_name}"


class Product(CreatedOnMixin):
    name = models.CharField(max_length=100)

    description = models.TextField()

    price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        validators=[MinValueValidator(0.01)]
    )

    in_stock = models.PositiveIntegerField(
        validators=[MinValueValidator(0)]
    )

    is_available = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.name}"


class Order(CreatedOnMixin):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='orders')

    products = models.ManyToManyField(Product, related_name='orders')

    total_price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        validators=[MinValueValidator(0.01)]
    )

    is_completed = models.BooleanField(default=False)

    def __str__(self):
        return f"Order by {self.profile.full_name} - Total: {self.total_price}"
