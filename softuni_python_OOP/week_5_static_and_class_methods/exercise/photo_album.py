from math import ceil

class PhotoAlbum:
    MAX_PHOTOS_PER_PAGE = 4

    def __init__(self, pages: int):
        self.pages = pages
        self.photos = [[] for _ in range(self.pages)]

    @classmethod
    def from_photos_count(cls, photos_count: int):
        return cls(ceil(photos_count / 4))

    def add_photo(self, label: str):

        for row in range(self.pages):
            if len(self.photos[row]) < self.MAX_PHOTOS_PER_PAGE:
                self.photos[row].append(label)
                return (f"{label} photo added successfully on page {row + 1} "
                        f"slot {self.photos[row].index(label) + 1}")
        return "No more free slots"

    def display(self):
        result = "-----------\n"
        for row in range(len(self.photos)):
            result += " ".join("[]" for label in self.photos[row])
            result += "\n-----------\n"

        return result

# album = PhotoAlbum(3)

# print(album.add_photo("baby"))
# print(album.add_photo("first grade"))
# print(album.add_photo("eight grade"))
# print(album.add_photo("party with friends"))
# print(album.photos)
# print(album.add_photo("prom"))
# print(album.add_photo("wedding"))

# for _ in range(8):
#     album.add_photo("asdf")
# print(album.display().strip())