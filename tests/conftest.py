import pytest

from src.Vacancy import Vacancy


@pytest.fixture
def area():
    area = [{
            "id": "113",
            "parent_id": None,
            "name": "Россия",
            "areas": [
                      {
                       "id": "1620",
                       "parent_id": "113",
                       "name": "Краснодарский край",
                       "areas": [
                                 {
                                  "id": "4228",
                                  "parent_id": "1620",
                                  "name": "Новороссийск",
                                  "areas": []
                                  }]
                      }]
            }]
    return area


@pytest.fixture
def vacancies2():
    vacancies = {"Тест прошел успешно!": "ok"}
    return vacancies


@pytest.fixture
def vacancy_obj():
    vacancy = Vacancy("Python Developer", "<https://hh.ru/vacancy/123456>",
                      "1000000 - 1500000 руб.", "Требования: опыт работы Python от 3 лет...")
    return vacancy


@pytest.fixture
def vacancy_list_obj():
    vacancy_1 = Vacancy("Python Developer", "<https://hh.ru/vacancy/123456>",
                        "90 000-100 000 руб.", "Требования: опыт работы от 3 лет...")
    vacancy_2 = Vacancy("Python Developer", "<https://hh.ru/vacancy/123456>",
                        "110 000-150 000 руб.", "Требования: опыт работы от 3 лет...")
    vacancy_list = [vacancy_1]
    vacancy_list.append(vacancy_2)
    return vacancy_list
