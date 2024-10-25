from django.contrib import admin

from MyPlantAppExamPrep3.plants.models import Plant


# Register your models here.
@admin.register(Plant)
class PlantAdmin(admin.ModelAdmin):
    list_display = ['type', 'name', 'description', 'price']
