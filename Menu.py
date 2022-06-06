from Books import Book
from Members import Member
from LendBooks import LendBook


class Menu:
    def search_books_menu():
        print('1. Search by book title ')
        print('2. Search by author name ')
        print('3. Search by ISBN ')
        print('4. Return ')
        print('')
        print('choose one of above options: ', end='')

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
