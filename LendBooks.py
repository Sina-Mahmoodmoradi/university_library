from datetime import date, timedelta
from pkgutil import get_data
from Books import Book
from Members import Member
from FileHandler import FileHandler as fl


class LendBook:
    def __init__(self, isbn, student_number, date_lend=date.today()) -> None:
        self.isbn = isbn
        self.student_number = student_number
        self.date_lend = date_lend
        self.date_return = date_lend + timedelta(days=7)

    def get_list(self):
        return [self.isbn, self.student_number, self.date_lend, self.date_return]

    def get_date(date_to_convert):
        return date.fromisoformat(date_to_convert)

    def lend(self):
        book = Book.get_book_by_isbn(self.isbn)
        if not book:
            print('ISBN does not match!')
            return
        if book.available == 0:
            print('this book is not available right now!')
            return

        member = Member.get_member_by_student_number(self.student_number)
        if not member:
            print('Student number does not match!')
            return
        if member.lent_books == 3:
            print('student has already have 3 books!')
            return
        book.lend_book()
        member.lend_book()
        fl.lend_book(self)
        print('done!')

    def return_book(self):
        records = fl.get_records_of_lent_books()
        record_key = False
        for key, r in enumerate(records):
            if r.student_number == self.student_number and r.isbn == self.isbn:
                record_key = key
        if record_key is False:
            print('This information does not match any records')
            return

        if self.date_lend > records[record_key].date_return:
            print(
                f'the book has been brought back {self.date_lend - records[record_key].date_return} day(s) late')

        Book.get_book_by_isbn(self.isbn).return_book()
        Member.get_member_by_student_number(self.student_number).return_book()
        del records[record_key]
        fl.rewrite_lendbook_file(records)
