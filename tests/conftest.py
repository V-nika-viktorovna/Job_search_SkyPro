import pytest


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
