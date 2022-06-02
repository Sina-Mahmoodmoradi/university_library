from mimetypes import init


class Member:
    def __init__(self, first_name, last_name, student_number, student_id, lent_books=0) -> None:
        self.first_name = first_name
        self.last_name = last_name
        self.student_number = student_number
        self.student_id = student_id
        self.lent_books = lent_books
