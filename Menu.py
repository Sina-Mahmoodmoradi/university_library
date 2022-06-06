from Books import Book
from Members import Member
from LendBooks import LendBook


class Menu:
    def search_books():
        print('1. Search by book title ')
        print('2. Search by author name ')
        print('3. Search by ISBN ')
        print('4. Return ')
        print('')
        print('choose one of above options: ', end='')

        choices = {
            '1': Menu.search_title,
            '2': Menu.search_author,
            '3': Menu.search_isbn,
            '4': lambda: 1,
        }

        Menu.looper(choices)

    def search_title():
        print('Enter book\'s title or part of it: ', end='')
        books = Book.get_book_by_title(input())
        if not books:
            print('There are no books with this title')
            print('Press any key to return: ', end='')
            input()
            return
        for book in books:
            Menu.print_book_information(book)

    def looper(choices):
        while(True):
            choice = input()
            if choice in choices:
                print('==================================================')
                choices[choice]()
            else:
                print(
                    f'{choice} is not an option. please enter one of available options: ', end='')
