from src.class__json import FileJSON
from src.class__user import User
from src.class__vacancy import Vacancies


def user_work():
    user_name = input("Введите ваше имя: ")
    user_keyword = input("Введите слово для поиска: ")
    new_user = User(user_name)
    vacancy_hh_list = new_user.get_vacancies(user_keyword)
    program_work = int(input("Выберите действие: \n"
                             "1 - Вывести список вакансий полученных с HH.ru.\n"
                             "2 - Добавить полученные вакансии в JSON файл.\n"
                             "3 - Удалить JSON файл.\n"
                             "4 - Вывести отсортированный список вакансий по заработной плате.\n"
                             "0 - Завершить работу.\n"))
    if program_work == 1:
        for vacancy in new_user.get_vacancies(user_keyword):
            vacancy_add = Vacancies.add_new_vacancy(vacancy)
            new_user.vacancies_list.append(vacancy_add)
        for vacancy in new_user.vacancies_list:
            print(f'{vacancy}\n')

    elif program_work == 2:
        file_json = FileJSON()
        file_json.file_save(vacancy_hh_list)

    elif program_work == 3:
        file_json = FileJSON()
        file_json.file_delete()

    elif program_work == 4:
        try:
            user_n_answer = int(input("Введите число для получения топ N вакансий: "))
        except ValueError:
            print("Введите число!")
            exit()
        for vacancy in new_user.get_vacancies(user_keyword):
            vacancy_add = Vacancies.add_new_vacancy(vacancy)
            new_user.vacancies_list.append(vacancy_add)
        for vacancy in new_user.get_vacancies_for_salary(user_n_answer):
            print(f'{vacancy}\n---\n')

    elif program_work == 0:
        print("Программа завершила работу.")
        exit()
    else:
        print("Неправильное действие.")
        user_work()
