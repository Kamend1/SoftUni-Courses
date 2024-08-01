import os
import django
from django.db.models import Q, Count, F

# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()

# Import your models here
from main_app.models import Profile, Product, Order


# Create queries within functions
def get_profiles(search_string=None):
    if search_string is None:
        return ""

    query_full_name = Q(full_name__icontains=search_string)
    query_email = Q(email__icontains=search_string)
    query_phone = Q(phone_number__icontains=search_string)

    profiles = Profile.objects.filter(query_full_name | query_email | query_phone).annotate(
        num_orders=Count('orders')).order_by('full_name')

    if not profiles.exists():
        return ""

    result = []

    for p in profiles:
        result.append(f"Profile: {p.full_name}, "
                      f"email: {p.email}, "
                      f"phone number: {p.phone_number}, "
                      f"orders: {p.num_orders}")

    return '\n'.join(result)


def get_loyal_profiles():
    profiles = Profile.objects.get_regular_customers()

    if not profiles.exists():
        return ""

    result = []

    for p in profiles:
        result.append(f"Profile: {p.full_name}, orders: {p.num_orders}")

    return '\n'.join(result)


def get_last_sold_products():

    order = Order.objects.order_by('-creation_date').first()

    if not order or not order.products.exists():
        return ""

    products = [p.name for p in order.products.all().order_by('name')]

    return f"Last sold products: {', '.join(products)}"


def get_top_products():
    products = Product.objects.prefetch_related('orders_products').annotate(num_sold=Count('orders_products')).filter(
        num_sold__gt=0).order_by('-num_sold', 'name')[:5]

    if not products.exists():
        return ""

    result = []

    for p in products:
        result.append(p.name + ", sold " + str(p.num_sold) + " times")

    return 'Top products:' + '\n' + "\n".join(result)


def apply_discounts():
    updated_orders = Order.objects.annotate(num_sold=Count('products')).filter(
        num_sold__gt=2,
        is_completed=False).update(total_price=F('total_price') * 0.9)

    return f"Discount applied to {updated_orders} orders."


def complete_order():
    order = Order.objects.prefetch_related('products').filter(is_completed=False).order_by(
        'creation_date').first()

    if not order:
        return ""

    order.is_completed = True
    order.save()

    for p in order.products.all():
        p.in_stock -= 1
        if p.in_stock == 0:
            p.is_available = False
        p.save()

    return "Order has been completed!"
