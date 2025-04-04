import json
import os.path


class Vacancy():
    """Класс для работы с вакансиями.
    Содердит методы сравнения вакансий между собой по зарплате и валидирует данные,
    которыми инициализируются его атрибуты."""

    job_title: str
    link_to_vacancy: str
    salary: str
    requirements: str

    def __init__(self, job_title, link_to_vacancy, salary, requirements):
        self.job_title = job_title
        self.link_to_vacancy = link_to_vacancy
        self.salary = salary
        self.requirements = requirements

    def __str__(self):

        result_dict = {
            'job_title': self.job_title,
            'link_to_vacancy': self.link_to_vacancy,
            'salary': self.salary,
            'requirements': self.requirements
        }

        return str(result_dict)

    @classmethod
    def cast_to_object_list(cls, file_json: str) -> list:
        """Метод принимает json файл с данными по вакансиям полученных по api
        и возвращает лист с объектами класса"""

        vacancys_list = []
        try:
            with open(file_json, 'r+', encoding='UTF-8') as f:
                vacancys_data = json.load(f)

        except FileNotFoundError as e:
            print(f'Файл не прочитан. Ошибка: {e}')

        else:
            for vacancy_dict in vacancys_data.get('items'):
                job_title = vacancy_dict.get('name')
                link_to_vacancy = vacancy_dict.get('alternate_url')

                if vacancy_dict.get('salary') is None:
                    salary_from = None
                    salary_to = None
                    salary_currency = ''
                else:
                    salary_from = vacancy_dict.get('salary').get('from')
                    salary_to = vacancy_dict.get('salary').get('to')
                    salary_currency = vacancy_dict.get('salary').get('currency')

                requirements = vacancy_dict.get('snippet').get("requirement")

                if salary_currency == 'RUR':
                    salary_currency = 'руб'
                elif salary_currency == 'USD':
                    salary_currency = 'usd'
                elif salary_currency == 'EUR':
                    salary_currency = 'eur'
                else:
                    salary_currency = 'валюта не задана'

                if salary_from is not None and salary_to is not None:
                    salary = f'{salary_from} - {salary_to} {salary_currency}'
                elif salary_from is not None and salary_to is None:
                    salary = f'{salary_from} {salary_currency}'
                else:
                    salary = 'Зарплата не указана'

                # result_dict = {
                #     'job_title': job_title,
                #     'link_to_vacancy_from': link_to_vacancy_from,
                #     'salary': salary,
                #     'requirements': requirements
                # }
                vacancys_obj = cls(job_title, link_to_vacancy, salary, requirements)
                vacancys_list.append(vacancys_obj)

        finally:
            return vacancys_list


if __name__ == '__main__':
    CURRENT_DIR = os.path.dirname(__file__)
    DATA_DIR = os.path.join(CURRENT_DIR, '..', 'data')
    json_file = os.path.join(DATA_DIR, 'vacancies.json')

    a = Vacancy.cast_to_object_list(json_file)

    for obj in a:
        print(obj)
        print(obj.job_title)
        print(obj.link_to_vacancy)
        print(obj.salary)
        print(obj.requirements)
        print('-------------------------')
