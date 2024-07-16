import json
import os.path
from abc import ABC, abstractmethod


class File(ABC):
    """
    Абстрактный класс для работы с файлами (открыть, сохранить, удалить).
    """
    @abstractmethod
    def file_open(self):
        """
        Абстрактный метод для открытия файла.
        """
        pass

    @abstractmethod
    def file_save(self, data):
        """
        Абстрактный метод для сохранения данных полученных с сайта в файл.
        :param data: Данные полученные с сайта.
        :return: Возвращает файл с данными.
        """
        pass

    @abstractmethod
    def file_delete(self):
        """
        Абстрактный метод для удаления файла.
        """
        pass


class FileJSON(File):
    """
    Класс для работы с JSON файлами.
    """
    def __init__(self):
        self.path = os.path.abspath("data/vacancies.json")

    def file_open(self):
        with open(self.path, "r", encoding='utf-8') as file:
            return json.load(file)

    def file_save(self, data):
        with open(self.path, "w", encoding='utf-8') as file:
            json.dump(data, file, ensure_ascii=False, indent=4)

    def file_delete(self):
        os.remove(self.path)
