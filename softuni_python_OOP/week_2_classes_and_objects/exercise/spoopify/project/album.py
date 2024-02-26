from project.song import Song

class Album:

    def __init__(self, name: str, *songs):
        self.name = name
        self.published = False
        self.songs = list(songs)

    def publish(self):
        if self.published == True:
            return f"Album {self.name} is already published."

        self.published = True
        return f"Album {self.name} has been published."

    def details(self):
        result = f"Album {self.name}"

        for song in self.songs:
            result += f"\n== {song.get_info()}"
        return result

    def add_song(self, song: Song):
        if song.single == True:
            return f"Cannot add {song.name}. It's a single"

        if self.published == True:
            return "Cannot add songs. Album is published."

        if song in self.songs:
            return "Song is already in the album."

        self.songs.append(song)
        return f"Song {song.name} has been added to the album {self.name}."

    def remove_song(self, song_name: str):
        if self.published == True:
            return "Cannot remove songs. Album is published."

        for song in self.songs:
            if song.name == song_name:
                self.songs.remove(song)
                return f"Removed song {song_name} from album {self.name}."

        return "Song is not in the album."

