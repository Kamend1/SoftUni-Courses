from project.library import Library
from unittest import TestCase, main

class TestLibrary(TestCase):

    def setUp(self):
        self.library = Library("Test")

    def test_object_has_attributes(self):
        self.assertTrue(hasattr(self.library, "books_by_authors"))
        self.assertTrue(hasattr(self.library, "readers"))

    def test_correct_init(self):
        self.assertEqual("Test", self.library.name)
        self.assertEqual({}, self.library.books_by_authors)
        self.assertEqual({}, self.library.readers)

    def test_name_set_correctly(self):
        library = Library("Test1")
        self.assertEqual("Test1", library.name)

    def test_name_raises_exception(self):
        with self.assertRaises(ValueError) as ve:
            new_library = Library("")

        self.assertEqual("Name cannot be empty string!", str(ve.exception))

    def test_add_book_author_not_in_collection(self):
        self.library.add_book("author1", "book1")
        self.assertEqual({"author1": ["book1"]}, self.library.books_by_authors)

    def test_add_book_author_in_collection(self):
        self.library.add_book("author1", "book1")
        self.library.add_book("author1", "book2")
        self.assertEqual({"author1": ["book1", "book2"]}, self.library.books_by_authors)

    def test_try_to_same_book_by_author_do_nothing(self):
        self.library.add_book("author1", "book1")
        self.library.add_book("author1", "book2")
        self.library.add_book("author1", "book2")
        self.assertEqual({"author1": ["book1", "book2"]}, self.library.books_by_authors)

    def test_add_new_reader_success(self):
        self.library.add_reader("reader1")
        self.assertEqual({"reader1": []}, self.library.readers)

    def test_add_existing_reader_returns_message(self):
        self.library.add_reader("reader1")
        result = self.library.add_reader("reader1")
        expected = "reader1 is already registered in the Test library."
        self.assertEqual(expected, result)

    def test_rent_book_author_does_not_exist(self):
        self.library.add_reader("reader1")
        result = self.library.rent_book("reader1", "author1", "book1")
        expected = "Test Library does not have any author1's books."
        self.assertEqual(expected, result)

    def test_rent_book_does_not_exist(self):
        self.library.add_reader("reader1")
        self.library.add_book("author1", "book1")
        result = self.library.rent_book("reader1", "author1", "book2")
        expected = """Test Library does not have author1's "book2"."""
        self.assertEqual(expected, result)

    def test_rent_book_reader_does_not_exist(self):
        result = self.library.rent_book("reader1", "author1", "book1")
        expected = "reader1 is not registered in the Test Library."
        self.assertEqual(expected, result)

    def test_rent_book_successful(self):
        self.library.add_reader("reader1")
        self.library.add_book("author1", "book1")
        self.library.rent_book("reader1", "author1", "book1")
        expected = {"reader1": [{"author1": "book1"}]}
        self.assertEqual(expected, self.library.readers)
        expected_books = {"author1": []}
        self.assertEqual(expected_books, self.library.books_by_authors)

if __name__ == '__main__':
    main()
