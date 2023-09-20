import sys
number_movies_ranked = int(input())
highest_ranking = -sys.maxsize
lowest_ranking = sys.maxsize
name_highest_ranking = ""
name_lowest_ranking = ""
sum_rating = 0

for i in range(number_movies_ranked):
    name_movie = input()
    ranking_movie = float(input())
    sum_rating += ranking_movie
    if ranking_movie > highest_ranking:
        highest_ranking = ranking_movie
        name_highest_ranking = name_movie
    if ranking_movie < lowest_ranking:
        lowest_ranking = ranking_movie
        name_lowest_ranking = name_movie

if number_movies_ranked != 0:
    average_ranking = sum_rating / number_movies_ranked
print(f"{name_highest_ranking} is with highest rating: {highest_ranking:.1f}")
print(f"{name_lowest_ranking} is with lowest rating: {lowest_ranking:.1f}")
print(f"Average rating: {average_ranking:.1f}")
