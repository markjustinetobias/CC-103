class Loan:
    def __init__(self, loan_id, book, member):
        self._loan_id = loan_id
        self._book = book
        self._member = member

        # Perform the loan
        self._book.borrow()
        self._member.borrow_book(self._book)

    def return_loan(self):
        self._book.return_book()
        self._member.return_book(self._book)
