# Generated by Django 5.0.4 on 2024-07-02 11:03

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0005_studentenrollment_student_subjects'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentenrollment',
            name='enrollment_date',
            field=models.DateField(default=datetime.date.today),
        ),
    ]
