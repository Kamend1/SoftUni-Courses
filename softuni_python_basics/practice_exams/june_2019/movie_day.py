time_movie_shoot = int(input())
number_scenes = int(input())
time_scene = int(input())

time_needed = 0.15 * time_movie_shoot + number_scenes * time_scene
difference = round(abs(time_movie_shoot - time_needed))

if time_movie_shoot >= time_needed:
    print(f"You managed to finish the movie on time! You have {difference} minutes left!")
else:
    print(f"Time is up! To complete the movie you need {difference} minutes.")
