class Book:
    def __init__(self, content: str):
        self.content = content


class Formatter:
    def format(self, book: Book) -> str:
        return book.content


class Printer:
    def get_book(self, book: Book, formatter: Formatter):
        # formatter = Formatter()
        formatted_book = formatter.format(book)
        return formatted_book

formatter = Formatter()
book = Book('some content')
printer = Printer()

print(printer.get_book(book, formatter))