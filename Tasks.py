from time import sleep
import os

def main():
    print('Введите действие:')
    print('1. Создание новой задачи')
    print('2. Изменение задачи')
    print('3. Вывод задач')
    answer = input()
    if answer == '1':
        pass
    elif answer == '2':
        pass
    elif answer == '3':
        pass
    else:
        print('Неверный запрос!')
        sleep(2)
        os.system('cls')
        main()


if __name__ == '__main__':
    main()
