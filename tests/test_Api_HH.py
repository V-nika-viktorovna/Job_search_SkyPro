import json
import os.path
from unittest.mock import patch

from src.Api_HH import ApiHH


@patch('requests.get')
def test_hh_get_city(mock_get, area):
    mock_get.return_value.json.return_value = area
    assert ApiHH().hh_get_city('Краснодарский край', 'Новороссийск') == 4228
    mock_get.assert_called_once()


@patch('requests.get')
def test_hh_get_city_error(mock_get, capsys):
    mock_get.return_value.json.return_value = [{}]
    assert ApiHH().hh_get_city('Краснодарский край', 'Новороссийск') == 0
    captured = capsys.readouterr()
    assert captured.out.split('id')[0] == "Код ответа: <MagicMock name='get().status_code' "
    mock_get.assert_called_once()


@patch('requests.get')
def test_hh_vacancies_try(mock_get, vacancies2):
    test_data = 1454
    text_data = 'Тест'

    CURRENT_DIR = os.path.dirname(__file__)
    DATA_DIR = os.path.join(CURRENT_DIR, '..', 'data')
    JSON_FILE = os.path.join(DATA_DIR, 'test_vacancies.json')

    mock_get.return_value.json.return_value = vacancies2
    test = ApiHH().hh_vacancies(text_data, test_data)

    with open(JSON_FILE, 'r', encoding='UTF-8') as f:
        data = json.load(f)

    assert test == data
    mock_get.assert_called_once()
