from datetime import date, timedelta
import Books
import Members
import FileHandler as fl


class LendBook:
    def __init__(self, isbn, student_number, date_lend) -> None:
        self.isbn = isbn
        self.student_number = student_number
        date_lend = date.today() if date_lend == '' else date.fromisoformat(date_lend)
        self.date_lend = date_lend
        self.date_return = date_lend + timedelta(days=7)

    def get_list(self):
        return [self.isbn, self.student_number, self.date_lend, self.date_return]

    def get_date(date_to_convert):
        return date.fromisoformat(date_to_convert)

    def lend(self):
        book = Books.Book.get_book_by_isbn(self.isbn)
        if not book:
            print('ISBN does not match!')
            return
        if book.available == 0:
            print('This book is not available right now!')
            return

        member = Members.Member.get_member_by_student_number(
            self.student_number)
        if not member:
            print('Student number does not match!')
            return
        if member.lent_books == 3:
            print('Student has already have 3 books!')
            return
        book.lend_book()
        member.lend_book()
        fl.FileHandler.lend_book(self)
        print('Done successfully!')

    def return_book(self):
        records = fl.FileHandler.get_records_of_lent_books()
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

        Books.Book.get_book_by_isbn(self.isbn).return_book()
        Members.Member.get_member_by_student_number(
            self.student_number).return_book()
        del records[record_key]
        fl.FileHandler.rewrite_lendbook_file(records)
        print('Done successfully!')

    def get_records_based_on_date_lend(date_lend):
        if date_lend == '':
            date_lend = str(date.today())
        records = fl.FileHandler.get_records_of_lent_books()
        results = []
        for record in records:
            if str(record.date_lend) == date_lend:
                results.append(record)
        return results

    def get_records_based_on_date_return(date_return):
        if date_return == '':
            date_return = str(date.today())
        records = fl.FileHandler.get_records_of_lent_books()
        results = []
        for record in records:
            if str(record.date_return) == date_return:
                results.append(record)
        return results

    def get_records_based_on_isbn(isbn):
        records = fl.FileHandler.get_records_of_lent_books()
        results = []
        for record in records:
            if record.isbn == isbn:
                results.append(record)
        return results

    def get_records_based_on_student_number(student_number):
        records = fl.FileHandler.get_records_of_lent_books()
        results = []
        for record in records:
            if record.student_number == student_number:
                results.append(record)
        return results
