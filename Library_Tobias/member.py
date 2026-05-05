class Member:
    def __init__(self, member_id, name, email):
        self._member_id = member_id
        self._name = name
        self._email = email
        self._borrowed_books = []

    def borrow_book(self, book):
        self._borrowed_books.append(book)

    def return_book(self, book):
        if book in self._borrowed_books:
            self._borrowed_books.remove(book)
