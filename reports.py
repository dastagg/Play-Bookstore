from datetime import datetime

from crud import Session
from models import Book
from sqlalchemy import and_, or_

s = Session()

print("All the books\n")
books = s.query(Book).all()

for book in books:
    print(f"Title: {book.title} - {book.price}")

print()

print("All the books filtered\n")

r = s.query(Book).filter_by(title="Deep Learning").first()
print("filter_by:", r)

r = s.query(Book).filter(Book.title == "Deep Learning").first()
print("filter:", r)
print()

results = (
    s.query(Book)
        .filter(and_(Book.pages > 750, Book.published > datetime(2016, 1, 1)))
        .all()
)

print(results)

s.close()
