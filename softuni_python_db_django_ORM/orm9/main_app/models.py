from django.db import models
from django.db.models.aggregates import Sum


class ProductManager(models.Manager):

    def available_products(self):
        return self.filter(is_available=True)

    def available_products_in_category(self, category_name: str):
        category_id = Category.objects.get(name=category_name)
        return self.filter(category=category_id, is_available=True)


class Category(models.Model):
    name = models.CharField(max_length=100)


class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    is_available = models.BooleanField(default=True)

    objects = ProductManager()

    def __str__(self):
        return f"{self.category.name}: {self.name}"


class Customer(models.Model):
    username = models.CharField(max_length=50, unique=True)


class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product, through='OrderProduct')


class OrderProduct(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
