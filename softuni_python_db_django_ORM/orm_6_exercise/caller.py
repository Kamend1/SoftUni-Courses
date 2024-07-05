import os
from datetime import date

import django
from django.db.models import QuerySet, Count, Avg, F
from django.utils.timezone import timedelta

# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()

# Import your models here
from main_app.models import Author, Book, Artist, Song, Product, Review, DrivingLicense, Driver, Owner, Car, \
    Registration


# Create queries within functions
def show_all_authors_with_their_books() -> str:
    result = []
    authors = Author.objects.all()

    for a in authors:
        if a.book_set.all().count() > 0:
            result.append(f"{a.name} has written - {', '.join(str(b) for b in a.book_set.all())}!")

    return '\n'.join(result)


def delete_all_authors_without_books() -> None:
    # authors = Author.objects.all()
    #
    # for a in authors:
    #     if a.book_set.all().count() == 0:
    #         a.delete()
    #
    Author.objects.filter(book__isnull=True).delete()


def add_song_to_artist(artist_name: str, song_title: str) -> None:
    artist = Artist.objects.get(name=artist_name)
    song = Song.objects.get(title=song_title)

    song.artists.add(artist)


def remove_song_from_artist(artist_name: str, song_title: str) -> None:
    artist = Artist.objects.get(name=artist_name)
    song = Song.objects.get(title=song_title)

    song.artists.remove(artist)


def get_songs_by_artist(artist_name: str) -> QuerySet:
    artist = Artist.objects.get(name=artist_name)

    return artist.songs.all().order_by('-id')


def calculate_average_rating_for_product_by_name(product_name: str) -> float:
    product = Product.objects.get(name=product_name)
    # reviews = product.reviews.all()
    #
    # avg_rating = sum(r.rating for r in reviews) / len(reviews)
    # return avg_rating

    avg_rating = product.reviews.aggregate(average_rating=Avg('rating'))['average_rating']
    return avg_rating
def get_reviews_with_high_ratings(threshold: int) -> QuerySet:
    high_ratings_reviews = Review.objects.filter(rating__gte=threshold)
    return high_ratings_reviews


def get_products_with_no_reviews() -> QuerySet:
    # products_without_reviews = Product.objects.annotate(count_reviews=Count('reviews')).filter(count_reviews=0).order_by('-name')
    # return products_without_reviews
    return Product.objects.filter(reviews__isnull=True).order_by('-name')

def delete_products_without_reviews():
    # Product.objects.annotate(count_reviews=Count('reviews')).filter(count_reviews=0).delete()
    get_products_with_no_reviews().delete()

def calculate_licenses_expiration_dates() -> str:
    licenses = DrivingLicense.objects.annotate(expiration_date=F('issue_date') + timedelta(days=365)).order_by('-license_number')

    result = [f"License with number: {l.license_number} expires on {l.expiration_date.strftime('%Y-%m-%d')}!" for l in licenses]

    return '\n'.join(result)


def get_drivers_with_expired_licenses(due_date: date) -> QuerySet:
    expired_licenses = DrivingLicense.objects.annotate(
        expiration_date=F('issue_date') + timedelta(days=365)
    ).order_by('-license_number').filter(expiration_date__gt=due_date)

    return Driver.objects.filter(license__in=expired_licenses)


def register_car_by_owner(owner: Owner) -> str:
    car = Car.objects.filter(owner__isnull=True).first()
    registration = Registration.objects.filter(car__isnull=True).first()

    car.owner = owner
    registration.car = car
    registration.registration_date = date.today()

    car.save()
    registration.save()

    return f"Successfully registered {car.model} to {owner.name} with registration number {registration.registration_number}."

# Create authors
# author1 = Author.objects.create(name="J.K. Rowling")
# author2 = Author.objects.create(name="George Orwell")
# author3 = Author.objects.create(name="Harper Lee")
# author4 = Author.objects.create(name="Mark Twain")
#
# # Create books associated with the authors
# book1 = Book.objects.create(
#     title="Harry Potter and the Philosopher's Stone",
#     price=19.99,
#     author=author1
# )
# book2 = Book.objects.create(
#     title="1984",
#     price=14.99,
#     author=author2
# )
#
# book3 = Book.objects.create(
#     title="To Kill a Mockingbird",
#     price=12.99,
#     author=author3
# )

# print(show_all_authors_with_their_books())
# delete_all_authors_without_books()

# # Create artists
# artist1 = Artist.objects.create(name="Daniel Di Angelo")
# artist2 = Artist.objects.create(name="Indila")
# # Create songs
# song1 = Song.objects.create(title="Lose Face")
# song2 = Song.objects.create(title="Tourner Dans Le Vide")
# song3 = Song.objects.create(title="Loyalty")

# # Add a song to an artist
# add_song_to_artist("Daniel Di Angelo", "Lose Face")
# add_song_to_artist("Daniel Di Angelo", "Loyalty")
# add_song_to_artist("Indila", "Tourner Dans Le Vide")

# songs = get_songs_by_artist("Daniel Di Angelo")
# for song in songs:
#     print(f"Daniel Di Angelo: {song.title}")

# # Get all songs by a specific artist
# songs = get_songs_by_artist("Indila")
# for song in songs:
#     print(f"Indila: {song.title}")
#
# # Remove a song from an artist
# remove_song_from_artist("Daniel Di Angelo", "Lose Face")
#
# # Check if the song is removed
# songs = get_songs_by_artist("Daniel Di Angelo")
#
# for song in songs:
#     print(f"Songs by Daniel Di Angelo after removal: {song.title}")

# # Create some products
# product1 = Product.objects.create(name="Laptop")
# product2 = Product.objects.create(name="Smartphone")
# product3 = Product.objects.create(name="Headphones")
# product4 = Product.objects.create(name="PlayStation 5")
#
# # Create some reviews for products
# review1 = Review.objects.create(description="Great laptop!", rating=5, product=product1)
# review2 = Review.objects.create(description="The laptop is slow!", rating=2, product=product1)
# review3 = Review.objects.create(description="Awesome smartphone!", rating=5, product=product2)

# print(calculate_average_rating_for_product_by_name("Laptop"))

# products_without_reviews = get_products_with_no_reviews()
# print(f"Products without reviews: {', '.join([p.name for p in products_without_reviews])}")

# # Create drivers
# driver1 = Driver.objects.create(first_name="Tanya", last_name="Petrova")
# driver2 = Driver.objects.create(first_name="Ivan", last_name="Yordanov")
#
# # Create licenses associated with drivers
# license1 = DrivingLicense.objects.create(license_number="123", issue_date=date(2022, 10, 6), driver=driver1)
#
# license2 = DrivingLicense.objects.create(license_number="456", issue_date=date(2022, 1, 1), driver=driver2)
#
# # Calculate licenses expiration dates
# expiration_dates = calculate_licenses_expiration_dates()
# print(expiration_dates)

# # Get drivers with expired licenses
# drivers_with_expired_licenses = get_drivers_with_expired_licenses(date(2023, 1, 1))
# print(drivers_with_expired_licenses)
# for driver in drivers_with_expired_licenses:
#     print(f"{driver.first_name} {driver.last_name} has to renew their driving license!")

# # Calculate licenses expiration dates
# expiration_dates = calculate_licenses_expiration_dates()
# print(expiration_dates)

# Create owners
# owner1 = Owner.objects.get(name='Ivelin Milchev')
# owner2 = Owner.objects.create(name='Alice Smith')
#
# # Create cars
# car1 = Car.objects.create(model='Citroen C5', year=2004)
# car2 = Car.objects.create(model='Honda Civic', year=2021)
#
# # Create instances of the Registration model for the cars
# registration1 = Registration.objects.create(registration_number='TX0044XA')
# registration2 = Registration.objects.create(registration_number='XYZ789')

# print(register_car_by_owner(owner1))
# registration = Registration.objects.get(registration_number='TX0044XA')
# print(registration.registration_date)