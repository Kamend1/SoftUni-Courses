# Generated by Django 3.2.7 on 2024-07-09 11:58

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import main_app.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField(validators=[main_app.models.validate_menu_categories])),
            ],
        ),
        migrations.CreateModel(
            name='Restaurant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, validators=[django.core.validators.MinLengthValidator(2, message='Name must be at least 2 characters long.'), django.core.validators.MaxLengthValidator(100, message='Name cannot exceed 100 characters.')])),
                ('location', models.CharField(max_length=200, validators=[django.core.validators.MinLengthValidator(2, message='Location must be at least 2 characters long.'), django.core.validators.MaxLengthValidator(200, message='Location cannot exceed 200 characters.')])),
                ('description', models.TextField(blank=True, null=True)),
                ('rating', models.DecimalField(decimal_places=2, max_digits=3, validators=[django.core.validators.MinValueValidator(0.0, message='Rating must be at least 0.00.'), django.core.validators.MaxValueValidator(5.0, message='Rating cannot exceed 5.00.')])),
            ],
        ),
        migrations.CreateModel(
            name='RestaurantReview',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('review_content', models.TextField()),
                ('rating', models.PositiveIntegerField(validators=[django.core.validators.MaxValueValidator(5)])),
                ('reviewer_name', models.CharField(max_length=100)),
                ('restaurant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.restaurant')),
            ],
            options={
                'verbose_name': 'Restaurant Review',
                'verbose_name_plural': 'Restaurant Reviews',
                'ordering': ['-rating'],
                'abstract': False,
                'unique_together': {('reviewer_name', 'restaurant')},
            },
        ),
        migrations.CreateModel(
            name='FoodCriticRestaurantReview',
            fields=[
                ('restaurantreview_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='main_app.restaurantreview')),
                ('food_critic_cuisine_area', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name': 'Food Critic Review',
                'verbose_name_plural': 'Food Critic Reviews',
                'ordering': ['-rating'],
            },
            bases=('main_app.restaurantreview',),
        ),
        migrations.CreateModel(
            name='RegularRestaurantReview',
            fields=[
                ('restaurantreview_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='main_app.restaurantreview')),
            ],
            options={
                'ordering': ['-rating'],
                'abstract': False,
            },
            bases=('main_app.restaurantreview',),
        ),
        migrations.CreateModel(
            name='MenuReview',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('review_content', models.TextField()),
                ('rating', models.PositiveIntegerField(validators=[django.core.validators.MaxValueValidator(5)])),
                ('reviewer_name', models.CharField(max_length=100)),
                ('menu', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.menu')),
            ],
            options={
                'verbose_name': 'Menu Review',
                'verbose_name_plural': 'Menu Reviews',
                'ordering': ['-rating'],
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='menu',
            name='restaurant',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.restaurant'),
        ),
        migrations.AddIndex(
            model_name='menureview',
            index=models.Index(fields=['menu'], name='main_app_menu_review_menu_id'),
        ),
        migrations.AlterUniqueTogether(
            name='menureview',
            unique_together={('reviewer_name', 'menu')},
        ),
    ]