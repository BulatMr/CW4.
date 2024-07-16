from abc import ABC, abstractmethod

import requests

from config import Hh_URL


class HhAPI(ABC):
    @abstractmethod
    def get_connect(self):
        pass

    @abstractmethod
    def get_load(self):
        pass


class Hh(HhAPI):
    """
    Класс для получения данных с сайта HH.
    """

    def __init__(self, keyword):
        self.url = Hh_URL
        self.params = {
            "name": keyword,
            "page": 0,
            "per_page": 100,
            "search_files": "name"
        }

    def get_connect(self):
        """
        Метод для подключения к стороннему сайту по URL.
        :return: Возвращает запрос.
        """
        return requests.get(self.url, params=self.params)

    def get_load(self):
        """
        Метод получения данных.
        :return: Возваращает данные в формате JSON.
        """
        vacancies_list = []

        while self.params.get("page") != 20:
            response = self.get_connect()
            vacancies = response.json()['items']
            vacancies_list.extend(vacancies)
            self.params["page"] += 1

        return vacancies_list
