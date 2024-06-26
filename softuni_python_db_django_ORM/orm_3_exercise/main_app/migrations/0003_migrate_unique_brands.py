# Generated by Django 5.0.4 on 2024-06-24 05:23

from django.db import migrations
from main_app.models import Shoe, UniqueBrands


class Migration(migrations.Migration):

    def add_unique_brands(apps, schema_editor):
        Shoe = apps.get_model("main_app", "Shoe")
        UniqueBrands = apps.get_model("main_app", "UniqueBrands")
        shoes = Shoe.objects.all()
        unique_brands = Shoe.objects.values_list("brand", flat=True).distinct()
        UniqueBrands.objects.bulk_create(brand_name=[brand_name for brand_name in unique_brands])


    def reverse_unique_brands(apps, schema_editor):
        UniqueBrands = apps.get_model("main_app", "UniqueBrands")
        UniqueBrands.objects.all().delete()

    dependencies = [
        ('main_app', '0002_uniquebrands'),
    ]

    operations = [migrations.RunPython(add_unique_brands, reverse_code=reverse_unique_brands)
    ]
