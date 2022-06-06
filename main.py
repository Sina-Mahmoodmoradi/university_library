from Menu import Menu
import os


with open('menu.txt', 'r') as file:
    cont = file.read()
    print(cont, end='')


choices = {
    # '1': Menu.search_books,
    # '2': Menu.search_students,
    # '3': Menu.edit_book,
    # '4': Menu.add_book,
    # '5': Menu.add_students,
    # '6': Menu.lend_book,
    # '7': Menu.return_book,
    # '8': Menu.reports,
    '9': quit,
}


def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


while(True):
    choice = input()
    if choice in choices:
        clear()
        print('==================================================')
        choices[choice]()
    else:
        print(
            f'{choice} is not a choice. please enter one of available options: ', end='')
