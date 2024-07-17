from time import sleep
from datetime import date
import os
import sqlite3

# начало работы с БД
def start_db():
    db = sqlite3.connect('Tasks.db')
    c = db.cursor()
    return db, c

# окончание работы с БД
def end_db(db):
    db.commit()
    db.close()

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
        
def else_time():
    birth_date = date(2006, 4, 1)  # год месяц число
    death_day = date(2066, 4, 1)
    today = date.today()
    delta = today - birth_date
    else_days = death_day - today
    print("Вы живете уже:", delta.days, "дней")
    print("Вам осталось жить:", else_days.days, "дней")

if __name__ == '__main__':
    main()
