import json
import os.path
from typing import Any

from src.JSON_Saver import JSONSaver
from src.Vacancy import Vacancy

CURRENT_DIR = os.path.dirname(__file__)
DATA_DIR = os.path.join(CURRENT_DIR, '..', 'data')


def json_read(path_file: str) -> Any:
    """Фунуция чтения json файла"""
    try:
        with open(path_file, 'r+', encoding='UTF-8') as f:
            data = json.load(f)
        return data
    except FileNotFoundError as e:
        print(f'Файл не прочитан. Ошибка: {e}')
        return []


def sorted_vacancy(vacancy_list: list[dict] | list[Vacancy]):
    """Сортировка списка вакансий по зарплате"""

    return sorted(vacancy_list, key=lambda x: int(x['salary'].split(' ')[0]), reverse=False)


def create_vacansy_list_file(json_f, filter_words='', salary_range=0, top_n=0):
    """Функция принимае путь до json файла с данными полученные от api HH, считывает данные из файла,
    формирует лист с обьектами класса Vacancy, сортируетего и добавляет словарь
    по каждому такому объекту в файл vacancy.json.
    Возвращает список словарей с вакансиями отфильтрованными по критериям"""

    vacancy_list = Vacancy.cast_to_object_list(json_f)
    vacancy_list.sort(reverse=True)

    result_list = []
    vacancy_saver = JSONSaver()
    for result_obj in vacancy_list:
        result_list.append(result_obj.to_dict())
        vacancy_saver.add_vacancy(result_obj)

    result_vacancy = vacancy_saver.filter_vacancies(filter_words, salary_range, top_n)

    return result_vacancy


if __name__ == '__main__':
    CURRENT_DIR = os.path.dirname(__file__)
    DATA_DIR = os.path.join(CURRENT_DIR, '..', 'data')
    json_file = os.path.join(DATA_DIR, 'vacancies.json')

    test_list = create_vacansy_list_file(json_file, 'продаж', 100000, 6)
    # test_sorted = sorted_vacancy(test_list)
    # print(test_sorted)
