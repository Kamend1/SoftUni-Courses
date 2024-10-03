# Generated by Django 5.1.1 on 2024-10-03 10:09

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('common', '0001_initial'),
        ('photos', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='to_photo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='photos.photo'),
        ),
        migrations.AddField(
            model_name='like',
            name='to_photo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='photos.photo'),
        ),
    ]
