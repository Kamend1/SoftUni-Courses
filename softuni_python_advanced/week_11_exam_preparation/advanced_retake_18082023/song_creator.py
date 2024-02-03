def add_songs(*songs):
    lyrics_dict = {}
    for song in songs:
        song_name = song[0]
        if song_name not in lyrics_dict:
            lyrics_dict[song_name] = []
        lyrics_dict[song_name] += song[1]

    result = ''
    for k, v in lyrics_dict.items():
        result += f"- {k}\n"
        for lyrics in v:
            result += f"{lyrics}\n"

    return result


print(add_songs(
    ("Bohemian Rhapsody", []),
    ("Just in Time",
     ["Just in time, I found you just in time",
      "Before you came, my time was running low",
      "I was lost, the losing dice were tossed",
      "My bridges all were crossed, nowhere to go"])
))
