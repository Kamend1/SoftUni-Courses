# Generated by Django 5.1.2 on 2024-10-22 06:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('album', '0002_alter_album_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='album',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
    ]
