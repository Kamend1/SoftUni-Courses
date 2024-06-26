# Generated by Django 5.0.4 on 2024-06-24 16:35

from django.db import migrations

def define_age_group(apps, schema_editor):
    person = apps.get_model('main_app', 'Person')
    persons = person.objects.all()
    for person in persons:
        if person.age <= 12:
            person.age_group = "Child"
            # person.save()
        elif 13 <= person.age <= 17:
            person.age_group = "Teen"
            # person.save()
        else:
            person.age_group = "Adult"
            # person.save()

    person.objects.bulk_update(persons, ['age_group'])


def reverse_age_group(apps, schema_editor):
    person = apps.get_model('main_app', 'Person')
    persons = person.objects.all()
    for person in persons:
        person.age_group = person._meta.get_field('age_group').default
        # person.save()
    person.objects.bulk_update(persons, ['age_group'])


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0009_item_order_person_smartphone'),
    ]

    operations = [migrations.RunPython(define_age_group, reverse_code=reverse_age_group)
    ]
