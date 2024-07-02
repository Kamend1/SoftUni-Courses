from typing import List


class Book:
    def __init__(self, title, author, location):
        self.title = title
        self.author = author
        self.location = location
        self.page = 0

    def turn_page(self, page):
        self.page = page

class Library:

    def __init__(self, books):
        self.books: List = books

    def find_book(self, title):
        try:
            book = next(filter(lambda b: b.title == title, self.books))
        except StopIteration:
            return f"No book with title {title}"

        return book


