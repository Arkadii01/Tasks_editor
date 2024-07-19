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

# создание новой задачи
def new_task():
    os.system('cls')
    print('0 - Выход')
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
                # создание задачи
                db, c = start_db()
                tasks_count = int(len(c.execute('SELECT id FROM Tasks').fetchall()))
                print(tasks_count)
                c.execute('INSERT INTO Tasks VALUES (?, ?, ?, ?)', (tasks_count+1, name, start, end)).fetchall()
                end_db(db)
                print('Задача создана!')
                sleep(2)
                new_task()

# создание имеющейся задачи
def change_task():
    os.system('cls')
    db, c = start_db()
    end_db(db)

# показ задачи (диаграмма Ганта, обычный список)
def show_task():
    os.system('cls')
    db, c = start_db()
    end_db(db)
    
# показ задачи (диаграмма Ганта, обычный список)
def else_time():
    os.system('cls')
    db, c = start_db()
    end_db(db)

# начальное окно
def main():
    os.system('cls')
    print('Введите действие:')
    print('1. Создание новой задачи')
    print('2. Изменение задачи')
    print('3. Вывод задач')
    print('4. Сколько осталось жить?')
    print('5. Настройки')
    print('6. Выход')
    answer = input()
    if answer == '1':
        new_task()
    elif answer == '2':
        pass
    elif answer == '3':
        pass
    elif answer == '4':
        pass
    elif answer == '5':
        pass
    elif answer == '6':
        pass
    else:
        print('Неверный запрос!')
        sleep(2)
        main()
        


if __name__ == '__main__':
    main()
