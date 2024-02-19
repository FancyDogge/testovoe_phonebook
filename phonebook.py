import pandas as pd
from colorama import init, Fore

from processors.phonebook_processors import ExcelFileProcessor


init(autoreset=True)

PHONEBOOK_FILENAME = 'phonebook.xlsx'


def display_page(entries: list, page_number: int, entries_per_page: int) -> None:
    """
    Ф-ция для отображения определенной страницы телефонной книги.
    """
    start = page_number * entries_per_page
    end = min(start + entries_per_page, len(entries))
    for i in range(start, end):
        print(f'{i+1}. {entries[i][0]} {entries[i][1]} {entries[i][2]}, {entries[i][3]}, {entries[i][4]}, {entries[i][5]}')


def display_entries(entries: list) -> None:
    """
    Отображает все записи в телефонной книге с учетом указанной пагинациии.
    """
    page_number = 0
    entries_per_page = int(input('Введите кол-во записей на одну страницу: '))
    
    while True:
        print('\nТекущая страница:', page_number + 1)
        display_page(entries, page_number, entries_per_page)

        user_input = input("Введите 'n' для перехода на следующую страницу, 'p' для предыдущей, 'q' для выхода: ").lower()
        
        if user_input == 'n':
            page_number += 1
        elif user_input == 'p' and page_number > 0:
            page_number -= 1
        elif user_input == 'q':
            break
        else:
            print(f"{Fore.RED}Некорректный ввод. Введите 'n', 'p', или 'q'.{Fore.RED}")


def add_entry(entries: list) -> None:
    """
    Ф-ция для добавления записи в телефонную книгу.
    """
    last_name = input('Введите фамилию: ')
    first_name = input('Введите имя: ')
    patronymic = input('Введите отчество: ') or None
    organization = input('Введите организацию: ')
    work_phone = input('Введите рабочий телефон: ') or None
    personal_phone = input('Введите личный телефон: ') or None
    entries.append((last_name, first_name, patronymic, organization, work_phone, personal_phone))
    print(f'{Fore.GREEN}Запись успешно создана!{Fore.GREEN}')


def edit_entry(entries: list) -> None:
    """
    Ф-ция для редактирования записи в телефонной книге.
    """
    last_name = input('Введите фамилию человека, чью запись отредактировать: ')
    found = False
    for i, entry in enumerate(entries):
        if entry[0] == last_name:
            found = True
            new_last_name = input('Введите новую фамилию (нажмите Enter чтобы пропустить): ') or last_name
            first_name = input('Введите новое имя (нажмите Enter чтобы пропустить): ') or entry[1]
            patronymic = input('Введите новое отчество (нажмите Enter чтобы пропустить): ') or entry[2]
            organization = input('Введите новое название организации (нажмите Enter чтобы пропустить): ') or entry[3]
            work_phone = input('Введите новый рабочий телефон (нажмите Enter чтобы пропустить): ') or entry[4]
            personal_phone = input('Введите новый личный телефон (нажмите Enter чтобы пропустить): ') or entry[5]
            entries[i] = (new_last_name, first_name, patronymic, organization, work_phone, personal_phone)
            print(f'{Fore.GREEN}Запись успешно обновлена!{Fore.GREEN}')
            break
    if not found:
        print(f'{Fore.RED}Запись не найдена!{Fore.RED}')


def search_entries(entries: list) -> None:
    """
    Ф-ция для поиска записи в телефонной книге.
    """
    search_term = input('Введите ключ для поиска (подойдут: имя, фамилия или организация): ')
    results = []
    for entry in entries:
        if search_term.lower() in entry[0].lower() or search_term.lower() in entry[1].lower() or search_term.lower() in entry[3].lower():
            results.append(entry)
    if results:
        for i, result in enumerate(results):
            print(f'{i+1}. {result[0]} {result[1]} {result[2]}, {result[3]}, {result[4]}, {result[5]}')
    else:
        print(f'{Fore.RED}Такой записи не существует!{Fore.RED}')


def main():
    file_processor = ExcelFileProcessor()

    filename = 'phonebook.xlsx'
    entries = file_processor.load_phonebook(filename)

    while True:
        print('Меню:')
        print('1. Отобразить записи')
        print('2. Добавить запись')
        print('3. Редактировать запись')
        print('4. Найти запись')
        print('5. Выход')

        choice = input('Введите свой выбор: ')

        if choice == '1':
            display_entries(entries)
        elif choice == '2':
            add_entry(entries)
        elif choice == '3':
            edit_entry(entries)
        elif choice == '4':
            search_entries(entries)
        elif choice == '5':
            file_processor.save_phonebook(filename, entries)
            print(f'{Fore.GREEN}Выход из программы. Файл сохранен.{Fore.GREEN}')
            break
        else:
            print(f'{Fore.RED}Неправильный выбор. Введите значения от 1 до 5.{Fore.RED}')

if __name__ == '__main__':
    main()