from FileHandler import FileHandler as fl


class Book:
    def __init__(self, title, author, year_of_publication, isbn, number_of_books, available=None) -> None:
        self.title = title
        self.author = author
        self.year_of_publication = year_of_publication
        self.isbn = isbn
        self.number_of_books = number_of_books
        self.available = available if available is not None else number_of_books

    def get_dict(self):
        return {'title': self.title,
                'author': self.author,
                'year_of_publication': self.year_of_publication,
                'isbn': self.isbn,
                'number_of_books': self.number_of_books,
                'available': self.available}

    def add_book(self):
        books = fl.get_all_books()
        if self.isbn in books:
            books[self.isbn].number_of_books += self.number_of_books
            books[self.isbn].available += self.number_of_books
        else:
            books[self.isbn] = self
        fl.add_books_to_file(books)

    def edit_book(self):
        books = fl.get_all_books()
        books[self.isbn] = self
        fl.add_books_to_file(books)

    def book_exists(isbn):
        return isbn in fl.get_all_books()

    def search_book_by_title(title):
        books = fl.get_all_books().values()
        results = filter(lambda book: title in book.title, books)
        return list(results)

    def search_book_by_author(author):
        books = fl.get_all_books().values()
        results = filter(lambda book: author in book.author, books)
        return list(results)

    def search_book_by_isbn(isbn):
        books = fl.get_all_books()
        if isbn in books:
            return books[isbn]
        else:
            return False
