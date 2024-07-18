from django.db import models
from django.db.models import Count


class CustomProfileManager(models.Manager):

    def get_regular_customers(self):

        return self.annotate(qty_orders=Count('orders')).filter(qty_orders__gt=2).order_by('-qty_orders')
