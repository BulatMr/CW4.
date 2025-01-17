import json
import os.path

from src.class__api import Hh
from src.class__vacancy import Vacancies


class User:
    def __init__(self, name):
        self.name = name
        self.vacancies_list = []

    @staticmethod
    def get_vacancies(keyword):
        """
        Метод получения вакансий.
        :param keyword: Ключевое слово для поиска вакансий.
        """
        vacancies = Hh(keyword)
        return Hh.get_load(vacancies)

    def get_vacancies_for_salary(self, n):
        """
        Метод для сортировки вакансий по зарплате.
        :param n: Количество вакансий.
        :return: Топ N вакансий по нижнему порогу зп.
        """
        sort_salary = list(sorted(self.vacancies_list, key=lambda x: x.salary_from, reverse=True))
        return sort_salary[:n]
