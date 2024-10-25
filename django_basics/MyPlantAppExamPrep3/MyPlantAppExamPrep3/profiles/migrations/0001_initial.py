# Generated by Django 5.1.2 on 2024-10-25 05:36

import MyPlantAppExamPrep3.profiles.validators
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=10, validators=[django.core.validators.MinLengthValidator(2)])),
                ('first_name', models.CharField(max_length=20, validators=[MyPlantAppExamPrep3.profiles.validators.FirstCapitalLetterValidator()])),
                ('last_name', models.CharField(max_length=20, validators=[MyPlantAppExamPrep3.profiles.validators.FirstCapitalLetterValidator()])),
                ('profile_picture', models.URLField(blank=True, null=True)),
            ],
        ),
    ]
