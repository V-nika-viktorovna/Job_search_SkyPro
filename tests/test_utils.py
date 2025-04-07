import os.path

from src.utils import create_vacansy_list_file


def test_create_vacansy_list_file(vacancy_obj, capsys):
    CURRENT_DIR = os.path.dirname(__file__)
    DATA_DIR = os.path.join(CURRENT_DIR, '..', 'data')
    json_file = os.path.join(DATA_DIR, 'vacancies.json')
    data_output = os.path.join(DATA_DIR, 'output.txt')

    result_vacancy = create_vacansy_list_file(json_file, 'продаж', 200000, 1)
    print(result_vacancy[0])
    captured = capsys.readouterr()
    assert captured.out == "{'job_title': 'Старший специалист отдела продаж', \
'link_to_vacancy': 'https://hh.ru/vacancy/118898540', 'salary': '200000 руб', \
'requirements': 'Опыт в продажах. Активная жизненная позиция. Желание зарабатывать \
от 200 000 рублей в месяц. Готовность работать много и с удовольствием.'}\n"

    with open(data_output, 'r', encoding='UTF-8') as f:
        data_txt = f.read()
    assert data_txt == 'Данная вакансия уже есть в списке\n'
