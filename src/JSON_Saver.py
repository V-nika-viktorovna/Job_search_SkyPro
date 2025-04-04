import json
import os.path

from src.ABC_JSON_Saver import ABCJSONSaver
from src.Vacancy import Vacancy

CURRENT_DIR = os.path.dirname(__file__)
DATA_DIR = os.path.join(CURRENT_DIR, '..', 'data')


class JSONSaver(ABCJSONSaver):
    """Класс для сохранения информации о вакансиях в JSON-файл."""

    def __init__(self):

        self.data = []

    def add_vacancy(self, vacancy='') -> None:
        if isinstance(vacancy, Vacancy):
            self.data.append(str(vacancy))

            CURRENT_DIR = os.path.dirname(__file__)
            DATA_DIR = os.path.join(CURRENT_DIR, '..', 'data')
            json_file = os.path.join(DATA_DIR, 'vacancy.json')

            with open(json_file, 'w+', encoding='UTF-8') as f:
                json.dump(self.data, f, indent=4)
            print('Вакансия успешно добавлена')
        else:
            print('Объект не является экземпляром класса Vacancy и не может быть добавлен')

    def delete_vacancy(self, vacancy=''):

        if isinstance(vacancy, Vacancy):

            json_file = os.path.join(DATA_DIR, 'vacancy.json')

            vacancy = str(vacancy)

            with open(json_file, 'r+', encoding='UTF-8') as f:
                vacancys_list = json.load(f)

            vacancys_list.remove(vacancy)

            with open(json_file, 'w+', encoding='UTF-8') as f:
                f.truncate(0)
                json.dump(vacancys_list, f, indent=4)
            print('Вакансия успешно удалена')
        else:
            print('Объект не является экземпляром класса Vacancy и не может удален')

    def filter_vacancies(self, filter_words='', salary_range=0, top_n=0):

        json_file = os.path.join(DATA_DIR, 'vacancy.json')

        with open(json_file, 'r+', encoding='UTF-8') as f:
            vacancys_list = json.load(f)

        filter_words = filter_words.lower()
        filter_words_vacancies_list = []

        for vacancys_str in vacancys_list:
            if filter_words != '':
                vacancys_dict = eval(vacancys_str)
                if (filter_words in vacancys_dict.get('job_title').lower() or
                        filter_words in vacancys_dict.get('requirements').lower()):
                    filter_words_vacancies_list.append(vacancys_dict)
            else:
                break

        filter_salary_vacancies_list = []

        if len(filter_words_vacancies_list) == 0:
            for vacancys_str in vacancys_list:
                vacancys_dict = eval(vacancys_str)
                if int(vacancys_dict.get('salary').split('-')[0]) >= salary_range:
                    filter_salary_vacancies_list.append(vacancys_dict)
        else:
            for filter_vacancies_dict in filter_words_vacancies_list:
                if int(filter_vacancies_dict.get('salary').split('-')[0]) >= salary_range:
                    filter_salary_vacancies_list.append(filter_vacancies_dict)

        result_vacancies_list = []

        if top_n > 0:
            for salary_vacancies_dict in filter_salary_vacancies_list:
                if top_n > 0:
                    result_vacancies_list.append(salary_vacancies_dict)
                    top_n -= 1
                else:
                    break
        else:
            result_vacancies_list = filter_salary_vacancies_list[0]

        return result_vacancies_list


if __name__ == '__main__':
    test_1 = 4242454
    test_2 = Vacancy('gffgfgf', 'gdfd', '', 'fnggfgf')
    test_3 = Vacancy('59995oololoo', 'gdfd', '2000000', '2000000')
    test_4 = Vacancy('шеф', 'gdfd', '60000', 'gfgfdfd шеф')
    test_5 = Vacancy('кок', 'gdfd', '100000', 'аваавава кок')
    test_6 = Vacancy('кок', 'gdfd', '500000', 'аваавава кок')
    test_7 = Vacancy('сторож', 'gdfd', '20000', 'сторож ппр')
    test_8 = Vacancy('59995o', 'gdfd', '10000', 'ппвавпавав 59995o')
    test_9 = Vacancy('кок', 'gdfd', '500000', 'аваавава кок')
    test_obj = JSONSaver()
    test_obj.add_vacancy(test_2)
    test_obj.add_vacancy(test_3)
    test_obj.add_vacancy(test_4)
    test_obj.add_vacancy(test_5)
    test_obj.add_vacancy(test_7)
    test_obj.add_vacancy(test_8)
    test_obj.add_vacancy(test_6)
    test_obj.add_vacancy(test_9)
    test_obj.delete_vacancy(test_2)

    print(test_obj.filter_vacancies('', 30000, 10))
