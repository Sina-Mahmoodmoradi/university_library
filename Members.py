import FileHandler as fl


class Member:
    def __init__(self, first_name, last_name, student_number, student_id, lent_books=0) -> None:
        self.first_name = first_name
        self.last_name = last_name
        self.student_number = student_number
        self.student_id = student_id
        self.lent_books = int(lent_books)

    def add_member(self):
        members = fl.FileHandler.get_all_members()
        members[self.student_number] = self
        fl.FileHandler.add_members_to_file(members)

    # use for check before adding new member
    def member_registered(student_number, student_id):
        students = fl.FileHandler.get_all_members()
        if student_number in students:
            return True
        for student in students.values():
            if student.student_id == student_id:
                return True
        return False

    def lend_book(self):
        members = fl.FileHandler.get_all_members()
        members[self.student_number].lent_books += 1
        fl.FileHandler.add_members_to_file(members)

    def return_book(self):
        members = fl.FileHandler.get_all_members()
        members[self.student_number].lent_books -= 1
        fl.FileHandler.add_members_to_file(members)

    def get_dict(self):
        return {
            'first_name': self.first_name,
            'last_name': self.last_name,
            'student_number': self.student_number,
            'student_id': self.student_id,
            'lent_books': self.lent_books
        }

    def get_member_by_last_name(last_name):
        members = fl.FileHandler.get_all_members().values()
        results = filter(lambda member: last_name in member.last_name, members)
        return list(results)

    def get_member_by_full_name(full_name):
        first_name, last_name = full_name.split()
        members = fl.FileHandler.get_all_members().values()
        results = filter(
            lambda member: last_name in member.last_name or first_name in member.first_name, members)
        return list(results)

    def get_member_by_student_id(student_id):
        members = fl.FileHandler.get_all_members().values()
        for member in members:
            if member.student_id == student_id:
                return member
        return False

    def get_member_by_student_number(student_number):
        members = fl.FileHandler.get_all_members()
        if student_number in members:
            return members[student_number]
        else:
            return False
