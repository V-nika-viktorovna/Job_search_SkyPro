from src.Vacancy import Vacancy


def test_str_Vacancy(vacancy_obj, capsys):
    print(vacancy_obj)
    captured = capsys.readouterr()
    assert captured.out == "'Название': Python Developer, \n\
'Ссылка на вакансию': <https://hh.ru/vacancy/123456>, \n\
'Зарплата': 1000000 - 1500000 руб., \n\
'Описание': Требования: опыт работы Python от 3 лет... \n"


def test_lt_Vacancy(vacancy_obj, vacancy_list_obj, capsys):
    vacancy_list_obj.append(vacancy_obj)
    vacancy_list_obj.sort()
    for vacancy in vacancy_list_obj:
        print(vacancy.salary)
    captured = capsys.readouterr()
    assert captured.out == '90 000-100 000 руб.\n110 000-150 000 руб.\n1000000 - 1500000 руб.\n'


def test_eq_Vacancy(vacancy_list_obj, capsys):
    if vacancy_list_obj[0].__eq__(vacancy_list_obj[1]):
        print('Метод сравнения работает иправно')
    captured = capsys.readouterr()
    assert captured.out == 'Метод сравнения работает иправно\n'


def test_valid_requirements_Vacancy():
    vacancy = Vacancy("Python Developer", "<https://hh.ru/vacancy/123456>",
                      "1000000 - 1500000 руб.", None)
    assert vacancy.requirements == 'Описание отсутствует'


def test_to_dict__Vacancy(vacancy_obj, capsys):
    print(vacancy_obj.to_dict())
    captured = capsys.readouterr()
    assert captured.out == "{'job_title': 'Python Developer', \
'link_to_vacancy': '<https://hh.ru/vacancy/123456>', \
'salary': '1000000 - 1500000 руб.', \
'requirements': 'Требования: опыт работы Python от 3 лет...'}\n"
