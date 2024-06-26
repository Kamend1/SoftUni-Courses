# Generated by Django 5.0.4 on 2024-06-24 16:37
from django.utils.timezone import timedelta

from django.db import migrations

def define_order(apps, schema_editor):
    order = apps.get_model('main_app', 'Order')
    orders = order.objects.all()
    for order in orders:
        if order.status == 'Pending':
            order.delivery = order.order_date + timedelta(days=3)
            order.save()
        elif order.status == 'Completed':
            order.warranty = "24 months"
            order.save()
        elif order.status == 'Cancelled':
            order.delete()

class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0012_define_smartphone_category'),
    ]

    operations = [migrations.RunPython(define_order)
    ]
