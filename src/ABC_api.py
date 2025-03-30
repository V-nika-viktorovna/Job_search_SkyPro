from abc import ABC, abstractmethod


class ApiAbc(ABC):

    @abstractmethod
    def hh_get_city(self):
        """Метод возвращает номер региона(города) для поиска вакансий,
        определенных в справочнике:
        https://api.hh.ru/openapi/redoc#tag/Obshie-spravochniki/operation/get-areas"""

        pass

    @abstractmethod
    def hh_vacancies(self):
        """Метод записывает полученные данные о вакансиях в json файл"""
        pass
