book_sought = input()
book_checked = input()
number_books = 0

while book_checked != book_sought:
    if book_checked == "No More Books":
        print(f"The book you search is not here!")
        print(f"You checked {int(number_books)} books.")
        break
    else:
        number_books += 1
        book_checked = input()
else:
    print(f"You checked {number_books} books and found it.")
