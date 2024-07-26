from django.core.validators import MinLengthValidator, RegexValidator
from django.db import models


# Create your models here.
class Category(models.Model):
    name = models.CharField(null=False, blank=False, unique=True, max_length=255)

    def __str__(self):
        return self.name

class Fruit(models.Model):
    name = models.CharField(null=False, blank=False, max_length=30,
                            validators=[MinLengthValidator(2),
                                        RegexValidator(regex=r"^[a-zA-Z]+",
                                                       message="Fruit name should contain only letters!")
                                        ],
                            )

    Image_url = models.URLField(null=False, blank=False)

    description = models.TextField(null=False, blank=False)

    nutrition = models.TextField(null=True, blank=True)

    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='fruits', null=True)

    def __str__(self):
        return self.name