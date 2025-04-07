import contextlib
import os.path

from src.JSON_Saver import JSONSaver
from src.Vacancy import Vacancy

CURRENT_DIR = os.path.dirname(__file__)
DATA_DIR = os.path.join(CURRENT_DIR, '..', 'data')


def create_vacansy_list_file(json_f, filter_words='', salary_range=0, top_n=0) -> list:
    """Функция принимае путь до json файла с данными полученные от api HH, считывает данные из файла,
    формирует лист с обьектами класса Vacancy, сортируетего и добавляет словарь
    по каждому такому объекту в файл vacancy.json.
    Возвращает список словарей с вакансиями отфильтрованными по критериям"""

    data_output = os.path.join(DATA_DIR, 'output.txt')

    vacancy_list = Vacancy.cast_to_object_list(json_f)
    vacancy_list.sort(reverse=True)

    if filter_words == '' and salary_range == 0 and top_n == 0:
        return vacancy_list

    result_list = []
    vacancy_saver = JSONSaver()
    for result_obj in vacancy_list:
        result_list.append(result_obj.to_dict())
        with open(data_output, 'w', encoding='UTF-8') as f:
            with contextlib.redirect_stdout(f):
                vacancy_saver.add_vacancy(result_obj)

    result_vacancy = vacancy_saver.filter_vacancies(filter_words, salary_range, top_n)

    return result_vacancy


if __name__ == '__main__':
    json_file = os.path.join(DATA_DIR, 'vacancies.json')

    test_list = create_vacansy_list_file(json_file, 'продаж', 100000, 6)
    # test_sorted = sorted_vacancy(test_list)
    # print(test_sorted)
