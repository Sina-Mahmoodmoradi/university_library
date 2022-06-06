from Books import Book
from Members import Member
from LendBooks import LendBook


class Menu:
    def search_books():
        print('1. Search by book name ')
        print('2. Search by author name ')
        print('3. Search by ISBN ')
        print('4. Return ')
        print('')
        print('choose one of above options: ', end='')

        choices = {
            '1': Menu.search_name,
            '2': Menu.search_author,
            '3': Menu.search_isbn,
            '4': lambda: 1,
        }

        Menu.looper(choices)

    def looper(choices):
        while(True):
            choice = input()
            if choice in choices:
                print('==================================================')
                choices[choice]()
            else:
                print(
                    f'{choice} is not an option. please enter one of available options: ', end='')
