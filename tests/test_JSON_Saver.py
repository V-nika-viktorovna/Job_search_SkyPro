import os.path

from src.JSON_Saver import JSONSaver

CURRENT_DIR = os.path.dirname(__file__)
DATA_DIR = os.path.join(CURRENT_DIR, '..', 'data')
JSON_FILE = os.path.join(DATA_DIR, 'test_vacancies.json')


def test_add_vacancy_and_delete_vacancy_JSONSaver_try(vacancy_list_obj, capsys):
    json_saver = JSONSaver()
    json_saver.add_vacancy(vacancy_list_obj[0])
    json_saver.add_vacancy(vacancy_list_obj[0])
    json_saver.delete_vacancy(vacancy_list_obj[0])
    captured = capsys.readouterr()
    assert captured.out.split('\n')[0] == 'Вакансия успешно добавлена'
    assert captured.out.split('\n')[1] == 'Данная вакансия уже есть в списке'
    assert captured.out.split('\n')[2] == 'Вакансия успешно удалена'


def test__and_delete_vacancy_JSONSaver_not_vacancy(vacancy_obj, capsys):
    json_saver = JSONSaver()
    test_data = 'это не вакансия'
    json_saver.delete_vacancy(vacancy_obj)
    json_saver.delete_vacancy(test_data)
    captured = capsys.readouterr()
    assert captured.out.split('\n')[0] == 'Данной вакансии нет в списке'
    assert captured.out.split('\n')[1] == 'Объект не является экземпляром класса Vacancy и не может удален'


def test_filter_vacancies_JSONSaver_filter_words(vacancy_obj, capsys):
    json_saver = JSONSaver()
    json_saver.add_vacancy(vacancy_obj)
    test_data = json_saver.filter_vacancies(filter_words='опыт работы Python')
    print(test_data)
    captured = capsys.readouterr()
    assert captured.out.split('\n')[1] == "[{'job_title': 'Python Developer', \
'link_to_vacancy': '<https://hh.ru/vacancy/123456>', \
'salary': '1000000 - 1500000 руб.', \
'requirements': 'Требования: опыт работы Python от 3 лет...'}]"
    json_saver.delete_vacancy(vacancy_obj)


def test_filter_vacancies_JSONSaver_filter_salary_top_n(vacancy_obj, capsys):
    json_saver = JSONSaver()
    json_saver.add_vacancy(vacancy_obj)
    test_data = json_saver.filter_vacancies(salary_range=1000000, top_n=10)
    print(test_data)
    captured = capsys.readouterr()
    assert captured.out.split('\n')[1] == "[{'job_title': 'Python Developer', \
'link_to_vacancy': '<https://hh.ru/vacancy/123456>', \
'salary': '1000000 - 1500000 руб.', \
'requirements': 'Требования: опыт работы Python от 3 лет...'}]"
    json_saver.delete_vacancy(vacancy_obj)
