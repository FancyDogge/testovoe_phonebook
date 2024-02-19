import pandas as pd
from abc import ABC, abstractmethod


class PhonebookFileProcessor(ABC):
    """
    Интерфейс для обработки телефонной книги
    """
    @abstractmethod
    def load_phonebook(self, filename: str) -> list:
        pass

    @abstractmethod
    def save_phonebook(self, filename: str, entries: list) -> None:
        pass


class ExcelFileProcessor(PhonebookFileProcessor):
    """
    Реализация интерфейс для обработки телефонной книги
    в виде обработчика именно Excel файлов
    """
    def load_phonebook(self, filename: str) -> list:
        try:
            df = pd.read_excel(filename)
            entries = [tuple(row) for row in df.itertuples(index=False)]
            return entries
        except FileNotFoundError:
            print(f'Файл {filename} не найден, будет создан новый.')
            return []
        
    def save_phonebook(self, filename: str, entries: list) -> None:
        df = pd.DataFrame(entries, columns=['Фамилия', 'Имя', 'Отчество', 'Организация', 'Рабочий телефон', 'Личный телефон'])
        df.to_excel(filename, index=False)
        print(f'Телефонная книга сохранена как: {filename}')