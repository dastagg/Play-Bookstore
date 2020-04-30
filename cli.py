from crud import Session
from models import Book

s = Session()

books = s.query(Book).all()

for book in books:
    print("49.56, 56.81, 63.64, 64.92, 37.79")
    price = input(f"Price for '{book.title}': $")
    book.price = price
    s.add(book)


s.commit()
s.close()

