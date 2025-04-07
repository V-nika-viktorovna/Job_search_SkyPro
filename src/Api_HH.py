import json
import os.path
from typing import Any

import requests

from src.ABC_api import ApiAbc

CURRENT_DIR = os.path.dirname(__file__)
DATA_DIR = os.path.join(CURRENT_DIR, '..', 'data')


class ApiHH(ApiAbc):
    """Класс для работы с платформой hh.ru.
    Подключаетчя к API и получает вакансии согдасно региона и города
    заданных для поиска."""

    def __init__(self):
        self.__url_get = "https://api.hh.ru"

    def hh_get_city(self, name_region: str, name_city: str) -> int:
        """Метод возвращает номер региона(города) для поиска вакансий,
        определенных в справочнике:
        https://api.hh.ru/openapi/redoc#tag/Obshie-spravochniki/operation/get-areas"""

        name_region = name_region.lower()
        name_city = name_city.lower()

        try:
            response = requests.get(self.__url_get + "/areas")
        except Exception as e:
            print(f'Ошибка при подключении: {e}')
            return 0
        else:
            try:
                result = response.json()

                for dicts in result[0].get("areas"):
                    if dicts.get("name").lower() == name_region:

                        id_region = dicts.get("id")

                        if int(id_region) == 1:
                            return 1
                        else:
                            for dict_region in dicts.get("areas"):

                                get_name_city = dict_region.get("name").lower()

                                if '(' in dict_region.get("name"):
                                    get_name_city = dict_region.get("name").split('(')[0].split(' ')[0].lower()

                                if dict_region.get("parent_id") == id_region and get_name_city == name_city:
                                    return int(dict_region.get("id"))

            except Exception as e:
                if response.status_code != 200:
                    print(f'Код ответа: {response.status_code}')
                    return 0
                else:
                    print(f'Ошибка: {e}')
                    return 0

    def hh_vacancies(self, text: str, get_city: int) -> Any:
        """Метод записывает полученные данные о вакансиях в json файл"""

        text.lower()

        while get_city is None or get_city == 0:
            print('Не введен регион для поиска вакансий')
            return 0

        else:
            json_file = os.path.join(DATA_DIR, 'vacancies.json')
            params = {
                'text': text,
                'area': get_city,
                'page': 0,
                'per_page': 100
            }

            try:
                response = requests.get(self.__url_get + '/vacancies', params=params)
            except Exception as e:
                with open(json_file, 'w+', encoding='UTF-8') as f:
                    print(f'Ошибка при подключении: {e}')
                    f.write(f'Ошибка при подключении: {e}')
            else:
                data = response.json()
                if response.status_code == 200:
                    with open(json_file, 'w+', encoding='UTF-8') as f:
                        json.dump(response.json(), f, indent=4)
                else:
                    print(f'Код ошибки: {response.status_code}')
                return data


if __name__ == '__main__':

    test_data = ApiHH().hh_get_city('краснодарский край', 'новороссийск')
    print(test_data)
    test = ApiHH().hh_vacancies('МенеджЕР по продажам', get_city=test_data)
    print(test)
