from turtle import title


class Book:
    def __init__(self, title, author, year_of_publication, isbn, number_of_books, available=0) -> None:
        self.title = title
        self.author = author
        self.year_of_publication = year_of_publication
        self.isbn = isbn
        self.number_of_books = number_of_books
        self.available = available
