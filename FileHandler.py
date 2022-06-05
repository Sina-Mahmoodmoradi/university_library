from csv import reader, DictWriter
from Books import Book


class FileHandler:
    def add_books_to_file(books):
        with open('books.csv', 'w') as file:
            writer = DictWriter(file,
                                fieldnames=['title', 'author', 'year_of_publication', 'isbn', 'number_of_books', 'available'])
            writer.writeheader()
            for book in books.values():
                writer.writerow(book.get_dict())

    def get_all_books():
        books = {}
        try:
            with open('books.csv', 'r') as file:
                reader = reader(file)
                next(reader)  # ignoring header

                for row in reader:
                    title, author, year_of_publication, isbn, number_of_books, available = row
                    books[isbn] = Book(
                        title, author, year_of_publication, isbn, number_of_books, available)
        except FileNotFoundError:
            pass
        return books
