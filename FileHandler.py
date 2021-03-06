from csv import reader as csv_reader, DictWriter, writer as csv_writer
import Books
import Members
import LendBooks
from os.path import exists


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
                reader = csv_reader(file)
                next(reader)  # ignoring header

                for row in reader:
                    title, author, year_of_publication, isbn, number_of_books, available = row
                    books[isbn] = Books.Book(
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
                reader = csv_reader(file)
                next(reader)  # ignoring header

                for row in reader:
                    first_name, last_name, student_number, student_id, lent_books = row
                    members[student_number] = Members.Member(
                        first_name, last_name, student_number, student_id, lent_books)
        except FileNotFoundError:
            pass
        return members

    def lend_book(lent_book):
        file_exists = exists('lendbook.csv')
        with open('lendbook.csv', 'a') as file:
            writer = csv_writer(file)
            if not file_exists:
                writer.writerow(['isbn', 'student_number',
                                'date_lend', 'date_return'])
            writer.writerow(lent_book.get_list())

    def rewrite_lendbook_file(lent_books):
        with open('lendbook.csv', 'w') as file:
            writer = csv_writer(file)
            writer.writerow(['isbn', 'student_number',
                            'date_lend', 'date_return'])

            for lent_book in lent_books:
                writer.writerow(lent_book.get_list())

    def get_records_of_lent_books():
        records = []
        try:
            with open('lendbook.csv', 'r') as file:
                reader = csv_reader(file)
                next(reader)  # ignoring header

                for row in reader:
                    isbn, student_number, date_lend, date_return = row
                    records.append(LendBooks.LendBook(
                        isbn, student_number, date_lend))
        except FileNotFoundError:
            pass
        return records
