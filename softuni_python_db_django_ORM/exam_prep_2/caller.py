import os
import django
from django.db.models import Q, Count, F, Case, When, Value, BooleanField

# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()

# Import your models here
from main_app.models import Profile, Product, Order


# Create queries within functions
def get_profiles(search_string=None):
    if search_string is None:
        return ""

    query = Q(full_name__icontains=search_string) | Q(email__icontains=search_string) | Q(phone_number__icontains=search_string)
    filtered_profiles = Profile.objects.filter(query).order_by('full_name')

    if not filtered_profiles:
        return ""

    result = []
    for p in filtered_profiles:
        # num_orders = Order.objects.filter(profile=p).count()
        num_orders = p.orders.count()
        result.append(f"Profile: {p.full_name}, email: {p.email}, phone number: {p.phone_number}, orders: {num_orders}")

    return '\n'.join(result)


def get_loyal_profiles():

    filtered_profiles = Profile.objects.get_regular_customers()

    if not filtered_profiles:
        return ""

    result = []

    for p in filtered_profiles:
        # num_orders = Order.objects.filter(profile=p).count()
        num_orders = p.orders.count()
        result.append(f"Profile: {p.full_name}, orders: {num_orders}")

    return '\n'.join(result)


def get_last_sold_products():

    order = Order.objects.prefetch_related('products').order_by('-creation_date').first()

    if not order or not order.products.exists():
        return ""

    # ordered_products = [p.name for p in order.products.all().order_by('name')]
    ordered_products = order.products.order_by('name').values_list('name', flat=True)
    return f"Last sold products: {', '.join(ordered_products)}"


def get_top_products():

    top_products = Product.objects.annotate(num_sold=Count('orders')).filter(num_sold__gt=0).order_by(
        '-num_sold',
        'name'
    )[:5]

    if not top_products.exists():
        return ""

    result = []

    for p in top_products:
        result.append(f"{p.name}, sold {p.num_sold} times")

    return "Top products:\n" + '\n'.join(result)


def apply_discounts():

    orders = Order.objects.annotate(num_products=Count('products')).filter(num_products__gt=2, is_completed=False).all()

    updated_orders = orders.update(total_price=F('total_price') * 0.9)

    return f"Discount applied to {updated_orders} orders."


def complete_order():

    order = Order.objects.filter(is_completed=False).order_by('creation_date').first()

    if order is None:
        return ""

    order.is_completed = True
    order.save()

    # for p in order.products.all():
    #     if p.in_stock >= 2:
    #         p.in_stock -= 1
    #         p.save()
    #     else:
    #         p.in_stock -= 1
    #         p.is_available = False
    #         p.save()

    Product.objects.filter(order=order).update(
        in_stock=F('in_stock') - 1,
        is_available=Case(
            When(in_stock=1, then=Value(False), default=F('is_available'), output_field=BooleanField())
        )
    )

    return "Order has been completed!"
