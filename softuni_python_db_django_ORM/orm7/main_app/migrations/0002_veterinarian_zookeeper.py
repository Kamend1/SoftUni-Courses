# Generated by Django 5.0.4 on 2024-07-05 10:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Veterinarian',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('phone_number', models.CharField(max_length=10)),
                ('license_number', models.CharField(max_length=10)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ZooKeeper',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('phone_number', models.CharField(max_length=10)),
                ('specialty', models.CharField(choices=[('Mammals', 'Mammals'), ('Birds', 'Birds'), ('Reptiles', 'Reptiles'), ('Others', 'Others')], max_length=10)),
                ('managed_animals', models.ManyToManyField(to='main_app.animal')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
