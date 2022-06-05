from csv import reader, DictWriter
from Books import Book
from Members import Member


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

    def add_members_to_file(members):
        with open('members.csv', 'w') as file:
            writer = DictWriter(file,
                                fieldnames=['first_name', 'last_name', 'student_number', 'student_id', 'lent_books'])
            writer.writeheader()
            for member in members.values():
                writer.writerow(member.get_dict())

    def get_all_members():
        members = {}
        try:
            with open('members.csv', 'r') as file:
                reader = reader(file)
                next(reader)  # ignoring header

                for row in reader:
                    first_name, last_name, student_number, student_id, lent_books = row
                    members[student_number] = Member(
                        first_name, last_name, student_number, student_id, lent_books)
        except FileNotFoundError:
            pass
        return members
