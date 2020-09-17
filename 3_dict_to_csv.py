"""

Домашнее задание №2

Работа csv

1. Создайте список словарей с ключами name, age и job и значениями по вашему выбору. 
   В списке нужно создать не менее 4-х словарей
2. Запишите содержимое списка словарей в файл в формате csv

"""
import csv


def main():
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
    people = [
        {'name': 'Paul', 'age': '37', 'job': 'driver'},
        {'name': 'Pam', 'age': '28', 'job': 'doctor'},
        {'name': 'Peter', 'age': '31', 'job': 'diver'},
        {'name': 'Philip', 'age': '24', 'job': 'dancer'},
    ]

    with open('export_names.csv', 'w', encoding='utf-8') as var:
        headers = ['name', 'age', 'job']
        writer = csv.DictWriter(var, headers, delimiter=';')
        writer.writeheader()
        for user in people:
            writer.writerow(user)


if __name__ == "__main__":
    main()
