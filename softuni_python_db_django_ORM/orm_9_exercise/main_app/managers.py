from decimal import Decimal

from django.db import models
from django.db.models import Count, Avg


class RealEstateListingManager(models.Manager):

    def by_property_type(self, property_type: str):
        return self.filter(property_type=property_type)

    def in_price_range(self, min_price: Decimal, max_price: Decimal):
        return self.filter(price__range=(min_price, max_price))

    def with_bedrooms(self, bedrooms_count: int):
        return self.filter(bedrooms=bedrooms_count)

    def popular_locations(self):
        popular_locations = self.values('location').annotate(location_count=Count('location')).order_by('-location_count', 'location')
        return list(popular_locations)[:2]


class VideoGameManager(models.Manager):

    def games_by_genre(self, genre: str):
        return self.filter(genre=genre)

    def recently_released_games(self, year: int):
        return self.filter(release_year__gte=year)

    def highest_rated_game(self):
        return self.order_by('rating').last()

    def lowest_rated_game(self):
        return self.order_by('rating').first()

    def average_rating(self):
        average_rating = self.aggregate(average_rating=Avg('rating'))
        result = float(average_rating['average_rating'])
        return f"{result:.1f}"
