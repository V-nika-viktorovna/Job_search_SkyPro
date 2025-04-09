import os.path

from src.Api_HH import ApiHH
from src.JSON_Saver import JSONSaver
from src.utils import create_vacansy_list_file
from src.Vacancy import Vacancy

CURRENT_DIR = os.path.dirname(__file__)
DATA_DIR = os.path.join(CURRENT_DIR, 'data')
json_file = os.path.join(DATA_DIR, 'vacancies.json')

# Создание экземпляра класса для работы с API сайтов с вакансиями
hh_api = ApiHH()

# Пример работы контструктора класса с одной вакансией
vacancy = Vacancy("Python Developer", "<https://hh.ru/vacancy/123456>",
                  "100 000-150 000 руб.", "Требования: опыт работы от 3 лет...")

# Сохранение информации о вакансиях в файл
json_saver = JSONSaver()
json_saver.add_vacancy(vacancy)
json_saver.delete_vacancy(vacancy)


# Функция для взаимодействия с пользователем
def user_interaction():

    while True:
        key_word = input('Введите ключевое слово для поиска вакансий:\nВвод:')
        if key_word:
            break
    while True:
        get_region_city = input('Введите регион и город поиска вакансий следуя примеру\n\
Например: Московская область, Балашиха\nВвод:')
        print('Выполняем поиск...')
        if get_region_city:
            try:
                if get_region_city.split(',')[1].split(' ')[1]:
                    break
            except IndexError:
                print('Вы не ввели регион или город')
                continue

    region = get_region_city.split(',')[0]
    city = get_region_city.split(',')[1].split(' ')[1]

    get_user_city = hh_api.hh_get_city(region, city)
    if get_user_city == 0:
        print('К сожалению ваш регион или город не найдены')

    get_user_vacancy = hh_api.hh_vacancies(key_word, get_user_city)
    if get_user_vacancy == 0 or len(get_user_vacancy) < 2:
        print('К сожалению по вашему запросу вакансии не найдены')
        return

    try:
        next_action = int(input('Список вакансий по вашему запросу готов.\
\nВведите номер действия, которое необходимо выполнить далее:\
\n1. Вывести полный список вакансий\n2. Отфильтровать список вакансий\nВвод:'))

    except ValueError:
        print('К сожалению вы ничего не выбрали')
        return

    if next_action == 1:
        user_vacancy = create_vacansy_list_file(json_file)
        for vacancy in user_vacancy:
            json_saver.add_vacancy(vacancy)
            print(f'{vacancy}\n______________________________________________')

    elif next_action == 2:
        try:
            next_action = int(input('Введите номер действия, по которому необходимо выполнить фильтрацию:\
\n1. По зарплате\n2. По ключевому слову\n3.По зарплате и по ключевому слову\nВвод:'))

        except ValueError:
            print('К сожалению вы ничего не выбрали')
            return

        if next_action == 1:
            try:
                user_salary = int(input('Введите от какой суммы зарплаты выводить вакансии\nВвод:'))
                ton_n = int(input('Если хотите увидеть все отфильтрованные вакансии, то введите 0,\
\nесли хотите увидеть топ вакансий, то введите количество необходимых вакансий\nВвод:'))

            except ValueError:
                print('К сожалению вы ничего не ввели')
                return

            else:
                user_salary_filter = create_vacansy_list_file(json_file, salary_range=user_salary, top_n=ton_n)
                for vacancy_filter in user_salary_filter:
                    vacancy_str = Vacancy(**vacancy_filter)
                    print(f'{vacancy_str}\n______________________________________________')

        elif next_action == 2:
            try:
                user_filter_words = input('Введите ключевое слово\nВвод:')
                ton_n = int(input('Если хотите увидеть все отфильтрованные вакансии, то введите 0,\
\nесли хотите увидеть топ вакансий, то введите количество необходимых вакансий\nВвод:'))

            except ValueError:
                print('К сожалению вы ничего не ввели')
                return

            else:
                user_salary_filter = create_vacansy_list_file(json_file, filter_words=user_filter_words, top_n=ton_n)
                for vacancy_filter in user_salary_filter:
                    vacancy_str = Vacancy(**vacancy_filter)
                    print(f'{vacancy_str}\n______________________________________________')

        elif next_action == 3:
            try:
                user_salary = int(input('Введите от какой суммы зарплаты выводить вакансии\nВвод:'))
                user_filter_words = input('Введите ключевое слово\nВвод:')
                ton_n = int(input('Если хотите увидеть все отфильтрованные вакансии, то введите 0,\
\nесли хотите увидеть топ вакансий, то введите количество необходимых вакансий\nВвод:'))

            except ValueError:
                print('К сожалению вы ничего не ввели')
                return

            else:
                user_salary_filter = create_vacansy_list_file(json_file, filter_words=user_filter_words,
                                                              salary_range=user_salary, top_n=ton_n)
                for vacancy_filter in user_salary_filter:
                    vacancy_str = Vacancy(**vacancy_filter)
                    print(f'{vacancy_str}\n______________________________________________')

        else:
            print('К сожалению вы ничего не выбрали')

    else:
        print('К сожалению вы ничего не выбрали')


if __name__ == '__main__':
    user_interaction()
