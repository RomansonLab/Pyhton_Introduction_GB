'''Создать телефонный справочник с
возможностью импорта и экспорта данных в
формате .txt. Фамилия, имя, отчество, номер
телефона - данные, которые должны находиться
в файле.
1. Программа должна выводить данные
2. Программа должна сохранять данные в
текстовом файле
3. Пользователь может ввести одну из
характеристик для поиска определенной
записи(Например имя или фамилию
человека)
4. Использование функций. Ваша программа
не должна быть линейной'''

from os.path import exists
from csv import DictReader, DictWriter


def get_info():
    flag = False
    while not flag:
        try:
            info = []
            last_name = input('Введите фамилию: ')
            first_name = input('Введите имя: ')
            info.append(last_name)
            info.append(first_name)
            phone_number = int(input('Введите номер телефона: '))
            if len(str(phone_number)) != 11:
                print('неверный номер')
            else:
                flag = True
                info.append(phone_number)
        except ValueError:
            print('not valid number')
    return info


def create_file():
    with open('phone.csv', 'w', encoding='utf-8') as data:
        # d Имя;Номер\n')
        f_n_writer = DictWriter(data, fieldnames=['Фамилия', 'Имя', 'Номер'])
        f_n_writer.writeheader()


def write_file(lst):
    with open('phone.csv', 'a', encoding='utf-8', newline='') as f_n:
        f_n_writer = DictWriter(f_n, fieldnames=['Фамилия', 'Имя', 'Номер'])
        f_n_writer.writerow({'Фамилия': lst[0], 'Имя': lst[1], 'Номер': lst[2]})


def read_file(file_name):
    # with open(file_name, encoding='utf-8') as data:
    #     phone_book = data.readlines()
    if exists(file_name):
        with open(file_name, 'r', encoding='utf-8') as f_n:
            f_n_reader = DictReader(f_n)
            phone_book = list(f_n_reader)
        return phone_book
    else:
        print('Файл не существует')
        return []


def delete_file(last_name):
    phone_book = read_file('phone.csv')
    updated_phone_book = [record for record in phone_book if 'Фамилия' in record and record['Фамилия'] != last_name]

    with open('phone.csv', 'w', encoding='utf-8', newline='') as f_n:
        f_n_writer = DictWriter(f_n, fieldnames=['Фамилия', 'Имя', 'Номер'])
        f_n_writer.writeheader()
        f_n_writer.writerows(updated_phone_book)

def change_number(last_name):
    phone_number = int(input('Введите новый номер телефона: '))
    phone_book = read_file('phone.csv')
    updated_phone_book = []

    for record in phone_book:
        if 'Фамилия' in record and record['Фамилия'] == last_name:
            record['Номер'] = phone_number
        updated_phone_book.append(record)

    with open('phone.csv', 'w', encoding='utf-8', newline='') as f_n:
        f_n_writer = DictWriter(f_n, fieldnames=['Фамилия', 'Имя', 'Номер'])
        f_n_writer.writeheader()
        f_n_writer.writerows(updated_phone_book)

def search_number(last_name):
    phone_book = read_file('phone.csv')
    for record in phone_book:
        if 'Фамилия' in record and record['Фамилия'] == last_name:
            print(record['Номер'])


def record_info():
    lst = get_info()
    write_file(lst)


def main():
    while True:
        command = input('Введите команду: ')
        if command == 'q':    #quit
            break
        elif command == 'r':  #read
            print(*read_file('phone.csv'))
        elif command == 'w':  #write
            if not exists('phone.csv'):
                create_file()
            record_info()
        elif command == 'd':  #delete
            last_name = input('Введите фамилию для удаления: ')
            if not exists('phone.csv'):
                print('Файл не существует')
            else:
                delete_file(last_name)
                print('Запись удалена.')
        elif command == 'c':  #change
            last_name = input('Введите фамилию у кого изменился номер: ')
            if not exists('phone.csv'):
                print('Файл не существует')
            else:
                change_number(last_name)
                print('Запись изменена')
        elif command == 's':  #search
            last_name = input('Введите фамилию для поиска: ')
            if not exists('phone.csv'):
                print('Файл не существует')
            else:
                search_number(last_name)


main()
