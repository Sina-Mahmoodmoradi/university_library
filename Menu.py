from Books import Book
from Members import Member
from LendBooks import LendBook


class Menu:

    # ========================================================================================================
    def search_books_menu():
        print('1. Search by book title ')
        print('2. Search by author name ')
        print('3. Search by ISBN ')
        print('4. Return ')
        print('')
        print('Choose one of above options: ', end='')
        choices = {
            '1': {'search_based_on': 'title or part of it', 'func': Book.get_book_by_title},
            '2': {'search_based_on': 'author name or part of their name', 'func': Book.get_book_by_author},
            '3': {'search_based_on': 'ISBN', 'func': Book.get_book_by_isbn},
            '4': 'return',
        }
        Menu.looper(choices, Menu.search_books)

    def print_book_information(book):
        print(f'Title: {book.title}')
        print(f'ISBN: {book.isbn}')
        print(f'Author: {book.author}')
        print(f'Published : {book.year_of_publication}')
        print(f'Total number of books : {book.number_of_books}')
        print(f'Available : {book.number_of_books}')

    def search_books(info):
        search_based_on, func = info.values()
        print(f'Enter book\'s {search_based_on}: ', end='')
        books = func(input())
        if not books:
            print('no book matches this info')
            print('Press any key to return: ', end='')
            input()
            return
        if not isinstance(books, list):
            books = [books]
        print('--------------------------------------------------')
        for book in books:
            Menu.print_book_information(book)
            print('--------------------------------------------------')
        print('Press any key to return: ', end='')
        input()

    # ========================================================================================================

    # ========================================================================================================

    def search_students_menu():
        print('1. Search by book last name')
        print('2. Search by full name ')
        print('3. Search by student number ')
        print('4. Search by ID number ')
        print('5. Return ')
        print('')
        print('Choose one of above options: ', end='')
        choices = {
            '1': {'search_based_on': 'last name or part of it', 'func': Member.get_member_by_last_name},
            '2': {'search_based_on': 'full name or part of it', 'func': Member.get_member_by_full_name},
            '3': {'search_based_on': 'student number', 'func': Member.get_member_by_student_number},
            '4': {'search_based_on': 'student ID', 'func': Member.get_member_by_student_id},
            '5': 'return',
        }
        Menu.looper(choices, Menu.search_students)

    def print_student_information(student):
        print(f'First name: {student.first_name}')
        print(f'Last name: {student.last_name}')
        print(f'ID: {student.student_id}')
        print(f'Student number : {student.student_number}')
        print(f'Number of lent books : {student.lent_books}')

    def search_students(info):
        search_based_on, func = info.values()
        print(f'Enter {search_based_on}: ', end='')
        students = func(input())
        if not students:
            print('no student matches this info')
            print('Press any key to return: ', end='')
            input()
            return
        if not isinstance(students, list):
            students = [students]
        print('--------------------------------------------------')
        for student in students:
            Menu.print_student_information(student)
            print('--------------------------------------------------')
        print('Press any key to return: ', end='')
        input()

    # ========================================================================================================

    def looper(choices, func):
        while(True):
            choice = input()
            if choices[choice] == 'return':
                return
            if choice in choices:
                print('==================================================')
                func(choices[choice])
            else:
                print(
                    f'"{choice}" is not an option. please enter one of available options: ', end='')
