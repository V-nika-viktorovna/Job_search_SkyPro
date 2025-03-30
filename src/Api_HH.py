import json
import os.path

import requests

from src.ABC_api import ApiAbc

CURRENT_DIR = os.path.dirname(__file__)
DATA_DIR = os.path.join(CURRENT_DIR, '..', 'data')


class ApiHH(ApiAbc):
    """Класс для работы с платформой hh.ru.
    Подключаетчя к API и получает вакансии согдасно региона и города
    заданных для поиска."""

    def __init__(self):
        self.url_get = "https://api.hh.ru"

    def hh_get_city(self, name_region: str, name_city: str) -> int:
        """Метод возвращает номер региона(города) для поиска вакансий,
        определенных в справочнике:
        https://api.hh.ru/openapi/redoc#tag/Obshie-spravochniki/operation/get-areas"""

        try:
            response = requests.get(self.url_get + "/areas")
        except Exception as e:
            print(f'Ошибка при подключении: {e}')
            return 0
        else:
            try:
                result = response.json()

                id_region = 0
                for dicts in result[0].get("areas"):
                    if dicts.get("name") == name_region:
                        id_region = dicts.get("id")

                    for dict_region in dicts.get("areas"):
                        if dict_region.get("parent_id") == id_region and dict_region.get("name") == name_city:
                            return int(dict_region.get("id"))

            except Exception as e:
                if response.status_code != 200:
                    print(f'Код ответа: {response.status_code}')
                    return 0
                else:
                    print(f'Ошибка: {e}')
                    return 0

    def hh_vacancies(self, get_city: int):
        """Метод записывает полученные данные о вакансиях в json файл"""

        json_file = os.path.join(DATA_DIR, 'vacancies.json')
        try:
            response = requests.get(self.url_get + f'/vacancies?area={get_city}')  # отправка GET-запроса

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

    test_data = ApiHH().hh_get_city('Краснодарский край', 'Новороссийск')
    test = ApiHH().hh_vacancies(1454)
    print(test)
