from FileHandler import FileHandler as fl


class Member:
    def __init__(self, first_name, last_name, student_number, student_id, lent_books=0) -> None:
        self.first_name = first_name
        self.last_name = last_name
        self.student_number = student_number
        self.student_id = student_id
        self.lent_books = lent_books

    def add_member(self):
        members = fl.get_all_members()
        members[self.student_number] = self
        fl.add_members_to_file(members)

    # use for check before adding new member
    def member_exists(student_number):
        return student_number in fl.get_all_members()

    def search_member_by_name(name):
        members = fl.get_all_members().values()
        results = filter(lambda member: name in member.name, members)
        return list(results)

    def search_member_by_author(student_id):
        members = fl.get_all_members().values()
        for member in members:
            if member.student_id == student_id:
                return member
        return False

    def search_member_by_isbn(student_number):
        members = fl.get_all_members()
        if student_number in members:
            return members[student_number]
        else:
            return False
