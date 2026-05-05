from book import Book
from member import Member
from loan import Loan

book = Book("B001", "Python Basics", "John Doe")
member = Member("M001", "Ana Cruz", "ana@email.com")
loan = Loan("L001", book, member)

print(book._title)
print(member._name)
print(loan._loan_id)
