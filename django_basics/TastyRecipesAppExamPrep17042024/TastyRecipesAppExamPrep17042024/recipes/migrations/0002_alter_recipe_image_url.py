# Generated by Django 5.1.2 on 2024-10-22 13:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='image_url',
            field=models.URLField(blank=True, null=True),
        ),
    ]