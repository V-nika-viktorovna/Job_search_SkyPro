import json
import os.path


class Vacancy():
    """Класс для работы с вакансиями.
    Содердит методы сравнения вакансий между собой по зарплате и валидирует данные,
    которыми инициализируются его атрибуты."""

    __slots__ = ('job_title', 'link_to_vacancy', 'salary', 'requirements')

    job_title: str
    link_to_vacancy: str
    salary: str
    requirements: str

    def __init__(self, job_title, link_to_vacancy, salary, requirements):
        self.job_title = job_title
        self.link_to_vacancy = link_to_vacancy
        self.salary = salary
        self.requirements = Vacancy.__valid_requirements(requirements)

    def __str__(self):

        if self.salary == 0:
            self.salary == 'Зарплата не указана'

        result_str = f"'Название': {self.job_title},\
 \n'Ссылка на вакансию': {self.link_to_vacancy},\
 \n'Зарплата': {self.salary},\
 \n'Описание': {self.requirements}\
 "
        return result_str

    def __lt__(self, other):
        vacancy_salary = int(self.salary.split(" ")[0])
        other_salary = int(other.salary.split(" ")[0])
        return vacancy_salary < other_salary

    def __eq__(self, other):
        return self.link_to_vacancy == other.link_to_vacancy

    def __valid_requirements(requirements):
        """Метод валидации для атрибута requirements"""

        if requirements is None:
            return 'Описание отсутствует'
        return requirements

    def to_dict(self):
        """Метод для представления данных о вакансии в словаре"""

        result_dict = {
            'job_title': self.job_title,
            'link_to_vacancy': self.link_to_vacancy,
            'salary': self.salary,
            'requirements': self.requirements
        }

        return result_dict

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

                if vacancy_dict.get('salary') is None:  # Валидация данных в ключе 'salary'
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
                    salary = "0"

                vacancys_obj = cls(job_title, link_to_vacancy, salary, requirements)
                vacancys_list.append(vacancys_obj)

        finally:
            return vacancys_list


if __name__ == '__main__':

    CURRENT_DIR = os.path.dirname(__file__)
    DATA_DIR = os.path.join(CURRENT_DIR, '..', 'data')
    json_file = os.path.join(DATA_DIR, 'vacancies.json')

    test_1 = Vacancy.cast_to_object_list(json_file)

    for obj in test_1:
        print(obj)
        print(obj.to_dict())
        print(obj.job_title)
        print(obj.link_to_vacancy)
        print(obj.salary)
        print(obj.requirements)
        print('-------------------------')
