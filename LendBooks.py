from datetime import date, timedelta
from Books import Book
from Members import Member
from FileHandler import FileHandler as fl


class LendBook:
    def __init__(self, isbn, student_number, date_lend=date.today()) -> None:
        self.isbn = isbn
        self.student_number = student_number
        self.date_lend = date_lend
        self.date_return = date_lend + timedelta(days=7)

    def lend(self):
        book = Book.get_book_by_isbn(self.isbn)
        if not book:
            print('ISBN does not match!')
            return
        if book.available == 0:
            print('book is not available!')
            return

        member = Member.get_member_by_student_number(self.student_number)
        if not member:
            print('Student number does not match!')
            return
        if member.lent_books == 3:
            print('student has already have 3 books!')
            return

        fl.lend_book(self)
        print('done!')
