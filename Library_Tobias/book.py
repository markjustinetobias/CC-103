class Book:
    def __init__(self, book_id, title, author):
        self._book_id = book_id
        self._title = title
        self._author = author
        self._available = True

    def borrow(self):
        if not self._available:
            raise Exception("Book is not available")
        self._available = False

    def return_book(self):
        self._available = True
