import os
import django
from django.db.models import Count, Avg, Q, F, Max

# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()

# Import your models here
from main_app.models import Director, Actor, Movie


# Create queries within functions
def get_directors(search_name=None, search_nationality=None):
    if search_name is None and search_nationality is None:
        return ""

    query = Q()
    if search_name:
        query &= Q(full_name__icontains=search_name)
    if search_nationality:
        query &= Q(nationality__icontains=search_nationality)

    directors = Director.objects.filter(query).order_by('full_name')

    if not directors.exists():
        return ""

    result = [
        f"Director: {d.full_name}, nationality: {d.nationality}, experience: {d.years_of_experience}"
        for d in directors
    ]

    return '\n'.join(result)


def get_top_director():
    top_director = Director.objects.get_directors_by_movies_count().first()

    if top_director is None:
        return ""

    return f"Top Director: {top_director.full_name}, movies: {top_director.movies_count}."


def get_top_actor():
    top_actor = Actor.objects.prefetch_related('starring_movies').annotate(
        movies_count=Count('starring_movies'),
        avg_rating=Avg('starring_movies__rating'),
    ).order_by(
        '-movies_count',
        'full_name',
    ).filter(movies_count__gt=0).first()

    if top_actor is None or not top_actor.starring_movies:
        return ""

    top_actor_movies = ', '.join(m.title for m in top_actor.starring_movies.all() if m)

    return (f"Top Actor: {top_actor.full_name}, "
            f"starring in movies: {top_actor_movies}, "
            f"movies average rating: {top_actor.avg_rating:.1f}")


def get_actors_by_movies_count():
    result = []
    actors = Actor.objects.prefetch_related('actor_movies').annotate(count_movies=Count('actor_movies')).filter(count_movies__gt=0).order_by(
        '-count_movies',
        'full_name')[:3]

    if not actors:
        return ""

    for a in actors:
        result.append(f"{a.full_name}, participated in {a.count_movies} movies")

    return '\n'.join(result)


def get_top_rated_awarded_movie():
    movie = Movie.objects.filter(is_awarded=True).select_related('starring_actor').\
        prefetch_related('actors').order_by('-rating', 'title').first()

    if not movie:
        return ""

    if not movie.starring_actor:
        starring_actor = 'N/A'
    else:
        starring_actor = movie.starring_actor.full_name

    return (f"Top rated awarded movie: {movie.title}, "
            f"rating: {movie.rating}. "
            f"Starring actor: {starring_actor}. "
            f"Cast: {', '.join(a.full_name for a in movie.actors.all().order_by('full_name'))}.")


def increase_rating():
    updated_movies = Movie.objects.filter(is_classic=True, rating__lte=9.9)

    if updated_movies.exists():
        updated_count = updated_movies.update(rating=F('rating') + 0.1)
        return f"Rating increased for {updated_count} movies."
    else:
        return "No ratings increased."
