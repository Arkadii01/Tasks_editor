from time import sleep
from datetime import date
import os
import sqlite3

def new_task():
    os.system('cls')
    print('Выход - 0')
    name = input('Введите название задачи:')
    if name == '':
        print('Название не должно быть пустым!')
        sleep(2)
        new_task()
    elif name == '0':
        main()
    else:
        start = input('Введите дату начала задачи (<номер_месяца>-<число>):')
        if start == '' or '-' not in start:
            print('Неверная дата!')
            sleep(2)
            new_task()
        elif start == '0':
            main()
        else:
            end = input('Введите дату окончания задачи (<номер_месяца>-<число>):')
            if end == '' or '-' not in end:
                print('Неверная дата!')
                sleep(2)
                new_task()
            elif end == '0':
                main()
            else:
                print(f'{name} {start} {end}')

def change_task():
    pass

def show_task():
    pass

def main():
    os.system('cls')
    print('Введите действие:')
    print('1. Создание новой задачи')
    print('2. Изменение задачи')
    print('3. Вывод задач')
    answer = input()
    if answer == '1':
        new_task()
    elif answer == '2':
        pass
    elif answer == '3':
        pass
    else:
        print('Неверный запрос!')
        sleep(2)
        main()

if __name__ == '__main__':
    main()
