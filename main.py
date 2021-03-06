from Menu import Menu
import os


def print_menu():
    with open('menu.txt', 'r') as file:
        cont = file.read()
        print(cont, end='')


choices = {
    '1': Menu.search_books_menu,
    '2': Menu.search_students_menu,
    '3': Menu.edit_book,
    '4': Menu.add_book,
    '5': Menu.add_student,
    '6': Menu.lend_book,
    '7': Menu.return_book,
    '8': Menu.reports_menu,
    '9': quit,
}


def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


print_menu()
while(True):
    choice = input()
    if choice in choices:
        clear()
        print('==================================================')
        choices[choice]()
        clear()
        print_menu()
    else:
        print(
            f'"{choice}" is not a choice. please enter one of available options: ', end='')
