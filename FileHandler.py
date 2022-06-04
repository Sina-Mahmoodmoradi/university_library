from csv import DictReader, DictWriter


class FileHandler:
    def add_books_to_file(books):
        with open('books.csv', 'w') as file:
            writer = DictWriter(file,
                                fieldnames=['title', 'author', 'year_of_publication', 'isbn', 'number_of_books', 'available'])
            writer.writeheader()
            for book in books:
                writer.writerow(book.get_dict())
