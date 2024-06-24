# Generated by Django 5.0.4 on 2024-06-24 16:36

from django.db import migrations


def define_phone_price(apps, schema_editor):
    MULTIPLIER = 120

    phone = apps.get_model('main_app', 'Smartphone')
    phones = phone.objects.all()

    for phone in phones:
        phone.price = MULTIPLIER * 120
        # phone.save()

    phone.objects.bulk_update(phones, ['price'])


def reverse_phone_price(apps, schema_editor):

    phone = apps.get_model('main_app', 'Smartphone')
    phones = phone.objects.all()

    for phone in phones:
        phone.price = phone._meta.get_field('price').default
        # phone.save()

    phone.objects.bulk_update(phones, ['price'])


def define_phone_category(apps, schema_editor):
    UPPER_DELIMITER = 750

    phone = apps.get_model('main_app', 'Smartphone')
    phones = phone.objects.all()

    for phone in phones:
        if phone.price >= UPPER_DELIMITER:
            phone.category = "Expensive"
            # phone.save()
        else:
            phone.category = "Cheap"
            # phone.save()

    phone.objects.bulk_update(phones,['category'])

def reverse_phone_category(apps, schema_editor):

    phone = apps.get_model('main_app', 'Smartphone')
    phones = phone.objects.all()

    for phone in phones:
        phone.category = phone._meta.get_field('category').default
        # phone.save()

    phone.objects.bulk_update(phones, ['category'])

class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0011_define_item_rarity'),
    ]

    operations = [migrations.RunPython(define_phone_price, reverse_code=reverse_phone_price),
                  migrations.RunPython(define_phone_category, reverse_code=reverse_phone_category)
    ]
