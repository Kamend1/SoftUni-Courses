from typing import List

from project.movie_specification.movie import Movie
from project.movie_specification.action import Action
from project.movie_specification.fantasy import Fantasy
from project.movie_specification.thriller import Thriller
from project.user import User


class MovieApp:

    def __init__(self):
        self.movies_collection: List[Action: Movie, Fantasy: Movie, Thriller: Movie] = []
        self.users_collection: List[User] = []

    def register_user(self, username: str, age: int):
        user = next(filter(lambda u: u.username == username, self.users_collection), None)

        if user:
            raise Exception("User already exists!")

        new_user = User(username, age)
        self.users_collection.append(new_user)
        return f"{username} registered successfully."

    def upload_movie(self, username: str, movie: Movie):
        user = next(filter(lambda u: u.username == username, self.users_collection), None)

        if not user:
            raise Exception("This user does not exist!")

        if movie.owner != user:
            raise Exception(f"{username} is not the owner of the movie {movie.title}!")

        if movie in self.movies_collection:
            raise Exception("Movie already added to the collection!")

        user.movies_owned.append(movie)
        self.movies_collection.append(movie)
        return f"{username} successfully added {movie.title} movie."

    def edit_movie(self, username: str, movie: Movie, **kwargs):
        if movie not in self.movies_collection:
            raise Exception(f"The movie {movie.title} is not uploaded!")

        user = next(filter(lambda u: u.username == username, self.users_collection), None)

        if movie not in user.movies_owned:
            raise Exception(f"{username} is not the owner of the movie {movie.title}!")

        for attribute, value in kwargs.items():
            setattr(movie, attribute, value)

        return f"{username} successfully edited {movie.title} movie."

    def delete_movie(self, username: str, movie: Movie):

        if movie not in self.movies_collection:
            raise Exception(f"The movie {movie.title} is not uploaded!")

        user = next(filter(lambda u: u.username == username, self.users_collection), None)

        if movie.owner != user:
            raise Exception(f"{username} is not the owner of the movie {movie.title}!")

        user.movies_owned.remove(movie)
        self.movies_collection.remove(movie)
        return f"{username} successfully deleted {movie.title} movie."

    def like_movie(self, username: str, movie: Movie):

        user = next(filter(lambda u: u.username == username, self.users_collection), None)

        if user == movie.owner:
            raise Exception(f"{username} is the owner of the movie {movie.title}!")

        if movie in user.movies_liked:
            raise Exception(f"{username} already liked the movie {movie.title}!")

        movie.likes += 1
        user.movies_liked.append(movie)
        return f"{username} liked {movie.title} movie."

    def dislike_movie(self, username: str, movie: Movie):

        user = next(filter(lambda u: u.username == username, self.users_collection), None)

        if movie not in user.movies_liked:
            raise Exception(f"{username} has not liked the movie {movie.title}!")

        movie.likes -= 1
        user.movies_liked.remove(movie)
        return f"{username} disliked {movie.title} movie."

    def display_movies(self):

        if len(self.movies_collection) == 0:
            return "No movies found."

        sorted_movies = sorted(self.movies_collection, key=lambda m: (-m.year, m.title))

        result = '\n'.join(m.details() for m in sorted_movies)

        return result

    # def __str__(self):
    #     result = (f"All users: {', '.join(u.username for u in self.users_collection)
    #     if self.users_collection else 'No users.'}")
    #
    #     result_1 = (f"All movies: {', '.join(m.title for m in self.movies_collection)
    #     if self.movies_collection else 'No movies.'}")
    #
    #     return result + "\n" + result_1

    def __str__(self):
        result = 'All users: '
        if not self.users_collection:
            result += 'No users.\n'
        else:
            result += ', '.join(u.username for u in self.users_collection) + '\n'

        result += 'All movies: '

        if not self.movies_collection:
            result += 'No movies.'
        else:
            result += ', '.join(m.title for m in self.movies_collection)

        return result
