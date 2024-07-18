from abc import ABC, abstractmethod

import requests
from requests import Response

from config import Hh_URL


class HhAPI(ABC):
    @abstractmethod
    def _get_connect(self):
        pass

    @abstractmethod
    def get_load(self):
        pass


class Hh(HhAPI):
    """
    Класс для получения данных с сайта HH.
    """

    def __init__(self, keyword):
        self._url = Hh_URL
        self._params = {
            "text": keyword,
            "page": 0,
            "per_page": 100,
            "search_files": "name"
        }

    def _get_connect(self):
        """
        Метод для подключения к стороннему сайту по URL.
        :return: Возвращает запрос.
        """
        return requests.get(self._url, params=self._params)

    def get_load(self):
        """
        Метод получения данных.
        :return: Возваращает данные в формате JSON.
        """
        vacancies_list = []

        while self._params.get("page") != 20:
            response = self._get_connect()
            check_response = self.check_status(response)
            if not check_response:
                print(f"Ошибка запроса данных: {response.status_code}")
            vacancies = response.json()['items']
            vacancies_list.extend(vacancies)
            self._params["page"] += 1

        return vacancies_list

    @staticmethod
    def check_status(response: Response) -> bool:
        """
        Метод проверки статуса подключения к сайту.
        """
        return response.status_code == 200
