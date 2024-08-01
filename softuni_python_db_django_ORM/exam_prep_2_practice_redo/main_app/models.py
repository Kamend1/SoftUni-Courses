from django.core.validators import MinLengthValidator, MinValueValidator
from django.db import models
from main_app.mixins import CreationDateMixin
from main_app.custom_managers import CustomProfileManager


# Create your models here.
class Profile(CreationDateMixin):
    full_name = models.CharField(max_length=100,
                                 validators=[MinLengthValidator(2),
                                             ],)

    email = models.EmailField()

    phone_number = models.CharField(max_length=15)

    address = models.TextField()

    is_active = models.BooleanField(default=True)

    objects = CustomProfileManager()


class Product(CreationDateMixin):
    name = models.CharField(max_length=100)

    description = models.TextField()

    price = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(0.01)])

    in_stock = models.PositiveIntegerField(validators=[MinValueValidator(0)])

    is_available = models.BooleanField(default=True)


class Order(CreationDateMixin):
    profile = models.ForeignKey('Profile', on_delete=models.CASCADE, related_name='orders')

    products = models.ManyToManyField('Product', related_name='orders_products')

    total_price = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(0.01)])

    is_completed = models.BooleanField(default=False)
