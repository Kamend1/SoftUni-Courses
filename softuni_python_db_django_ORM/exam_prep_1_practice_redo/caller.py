import os
import django
from django.db.models import Q, F, Count, Avg

# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()

# Import your models here
from main_app.models import Director, Actor, Movie


# Create queries within functions
def get_directors(search_name=None, search_nationality=None):
    query_name = Q(full_name__icontains=search_name)
    query_nationality =Q(nationality__icontains=search_nationality)
    result = []

    if search_name is None and search_nationality is not None:
        directors = Director.objects.filter(query_nationality).order_by('full_name')
    elif search_name is not None and search_nationality is None:
        directors = Director.objects.filter(query_name).order_by('full_name')
    elif search_name is not None and search_nationality is not None:
        directors = Director.objects.filter(query_name & query_nationality).order_by('full_name')
    else:
        return ""

    for d in directors:
        result.append(f"Director: {d.full_name}, nationality: {d.nationality}, experience: {d.years_of_experience}")

    return '\n'.join(result)


def get_top_director():
    director = Director.objects.get_directors_by_movies_count().filter(num_movies__gt=0).first()

    if not director:
        return ""

    return f"Top Director: {director.full_name}, movies: {director.num_movies}."


def get_top_actor():
    top_actor = Actor.objects.annotate(
        num_movies=Count('starring_actor_movies'),
        avg_rating=Avg('starring_actor_movies__rating')
    ).filter(
        num_movies__gt=0
    ).order_by(
        '-num_movies',
        'full_name'
    ).first()

    if not top_actor:
        return ""

    movies = [m.title for m in top_actor.starring_actor_movies.all()]

    return (f"Top Actor: {top_actor.full_name}, "
            f"starring in movies: {', '.join(movies)}, "
            f"movies average rating: {top_actor.avg_rating:.1f}")


def get_actors_by_movies_count():
    actors = Actor.objects.prefetch_related('movies_actors').annotate(
        num_movies=Count('movies_actors')
    ).filter(num_movies__gt=0).order_by(
        '-num_movies',
        'full_name',
    )[:3]

    if not actors.exists():
        return ""

    result = []

    for a in actors:
        result.append(f"{a.full_name}, participated in {a.num_movies} movies")

    return '\n'.join(result)


def get_top_rated_awarded_movie():
    movie = Movie.objects.prefetch_related('starring_actor', 'actors').filter(is_awarded=True).order_by(
        '-rating',
        'title',
    ).first()

    if not movie:
        return ""

    if not movie.starring_actor:
        starring_actor = 'N/A'
    else:
        starring_actor = movie.starring_actor.full_name

    participating_actors = [a.full_name for a in movie.actors.all()]

    return (f"Top rated awarded movie: {movie.title}, "
            f"rating: {movie.rating}. "
            f"Starring actor: {starring_actor}. "
            f"Cast: {', '.join(participating_actors)}.")


def increase_rating():

    updated_movies = Movie.objects.filter(is_classic=True).filter(rating__lt=10).update(rating=F('rating') + 0.1)

    if updated_movies == 0:
        return "No ratings increased."
    else:
        return f"Rating increased for {updated_movies} movies."
