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
            Menu.return_to_previous_menu()
            return
        if not isinstance(books, list):
            books = [books]
        print('--------------------------------------------------')
        for book in books:
            Menu.print_book_information(book)
            print('--------------------------------------------------')
        Menu.return_to_previous_menu()

    # ========================================================================================================
    def add_book():
        book = Menu.make_book_object()
        book.add_book()
        Menu.return_to_previous_menu()

    def edit_book():
        print('Enter book\'s ISBN: ', end='')
        isbn = input()
        if Book.book_exists(isbn):
            book = Menu.make_book_object()
            print('Number of available books: ', end='')
            book.available = int(input())
            if book.edit(isbn):
                print('Book edited successfully')
            else:
                print('Fail! ISBN already exists!')
        else:
            print('no book matches this info')
        Menu.return_to_previous_menu()
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
            Menu.return_to_previous_menu()
            return
        if not isinstance(students, list):
            students = [students]
        print('--------------------------------------------------')
        for student in students:
            Menu.print_student_information(student)
            print('--------------------------------------------------')
        Menu.return_to_previous_menu()

    # ========================================================================================================
    def add_student():
        print('Enter following information:')
        print('First_name: ', end='')
        first_name = input()
        print('Last name: ', end='')
        last_name = input()
        print('Student number: ', end='')
        student_number = input()
        print('ID: ', end='')
        student_id = input()
        if Member.member_registered(student_number, student_id):
            print('Member with this information is already registered!')
        else:
            Member(first_name, last_name, student_number,
                   student_id).add_member()
            print('Member registered successfully!')
        Menu.return_to_previous_menu()

    # ========================================================================================================
    def lend_book():
        lent_book = Menu.make_lend_book_object()
        lent_book.lend()
        Menu.return_to_previous_menu()

    def return_book():
        lent_book = Menu.make_lend_book_object()
        lent_book.return_book()
        Menu.return_to_previous_menu()

    def make_lend_book_object():
        print('Enter following information:')
        print('student number: ', end='')
        student_number = input()
        print('ISBN: ', end='')
        isbn = input()
        print('date (form: yyyy-mm-dd) (leave empty for today) : ', end='')
        date = input()
        return LendBook(isbn, student_number, date)

    # ========================================================================================================
    def reports_menu():
        print('1. Lent books based on date lend')
        print('2. Lent books based on date return')
        print('3. Lent books based on ISBN')
        print('4. Lent books based on student number')
        print('5. Return ')
        print('')
        print('Choose one of above options: ', end='')
        choices = {
            '1': {'search_based_on': 'date lend (form:yyyy-mm-dd)(leave empty for today)', 'func': LendBook.get_records_based_on_date_lend},
            '2': {'search_based_on': 'date return (form:yyyy-mm-dd)(leave empty for today)', 'func': LendBook.get_records_based_on_date_return},
            '3': {'search_based_on': 'ISBN', 'func': LendBook.get_records_based_on_isbn},
            '4': {'search_based_on': 'student number', 'func': LendBook.get_records_based_on_student_number},
            '5': 'return',
        }
        Menu.looper(choices, Menu.search_records)

    def search_records(info):
        search_based_on, func = info.values()
        print(f'Enter {search_based_on}: ', end='')
        records = func(input())
        if not records:
            print('no record matches this info')
            Menu.return_to_previous_menu()
            return
        print('--------------------------------------------------')
        for record in records:
            Menu.print_record(record)
            print('--------------------------------------------------')
        Menu.return_to_previous_menu()

    def print_record(record):
        print(f'Student number: {record.student_number}')
        print(f'ISBN: {record.isbn}')
        print(f'Date lend: {record.date_lend}')
        print(f'Date return: {record.date_return}')

    # ========================================================================================================
    def make_book_object():
        print('Enter following information:')
        print('Title: ', end='')
        title = input()
        print('Author: ', end='')
        author = input()
        print('ISBN: ', end='')
        isbn = input()
        print('Published: ', end='')
        published = input()
        print('Number of books: ', end='')
        number_of_books = int(input())
        return Book(title, author, published, isbn, number_of_books)

    def looper(choices, func):
        while(True):
            choice = input()
            if choice in choices:
                if choices[choice] == 'return':
                    return
                print('==================================================')
                func(choices[choice])
                return
            else:
                print(
                    f'"{choice}" is not an option. please enter one of available options: ', end='')

    def return_to_previous_menu():
        print('Press Enter to return: ', end='')
        input()
