def movie_organizer(*movies):
    movies_dict = {}
    result = ""

    for movie in movies:
        if not movie[1] in movies_dict:
            movies_dict[movie[1]] = []
        movies_dict[movie[1]].append(movie[0])

    sorted_movies_dict = dict(sorted(movies_dict.items(), key=lambda x: (-len(x[1]), x[0])))

    for k, v in sorted_movies_dict.items():
        result += f"{k} - {len(v)}\n"
        for el in sorted(v):
            result += f"* {el}\n"

    return result

print(movie_organizer(
    ("The Matrix", "Sci-fi")))
