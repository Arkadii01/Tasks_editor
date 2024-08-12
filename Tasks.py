import matplotlib.pyplot as plt
import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QButtonGroup
import sqlite3
import numpy as np
from datetime import datetime
import os


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('main_window.ui', self)
        self.save_mod = ''
        self.type = ''
        self.dates = []
        
        self.area_name.setPlaceholderText('Введите название задачи')
        self.area_start.setPlaceholderText('Нач. дата (пример: 07.31, 12.01)')
        self.area_end.setPlaceholderText('Кон. дата (пример: 07.31, 12.01)')
        self.area_task_num.setPlaceholderText('Введите номер задачи')
        
        self.btn_create.clicked.connect(self.create)
        self.btn_change.clicked.connect(self.change)
        self.btn_delete.clicked.connect(self.delete)
        self.btn_output.clicked.connect(self.output)
        self.btn_else.clicked.connect(self.time_else)
        self.btn_settings.clicked.connect(self.settings)
        self.btn_clear.clicked.connect(self.clear)
        
        self.btn_back.clicked.connect(self.back)
        self.btn_save.clicked.connect(self.save)
        self.btn_take.clicked.connect(self.take)
        self.btn_type_get.clicked.connect(self.show_type)
        self.btn_delete_everything.clicked.connect(self.delete_everything)
        
        self.radio_group = QButtonGroup(self)
        self.radio_group.addButton(self.radio_gante)
        self.radio_group.addButton(self.radio_list)
        self.radio_gante.toggled.connect(self.radio_change)
        self.radio_list.toggled.connect(self.radio_change)
        self.radio_theme = QButtonGroup(self)
        self.radio_theme.addButton(self.radio_dark)
        self.radio_theme.addButton(self.radio_light)
        
        self.tasks = []
        self.tasks_get()
        
    def start_db(self):
        self.db = sqlite3.connect('Tasks.db')
        self.c = self.db.cursor()
    
    def end_db(self):
        self.db.commit()
        self.db.close()
    
    def tasks_get(self):
        self.start_db()
        self.tasks = self.c.execute('SELECT * FROM Tasks').fetchall()
        self.end_db()
        print(self.tasks)
        
    def create(self):
        self.clear()
        self.save_mod = 'create'
        self.text_create.show() 
        self.area_name.show()
        self.area_start.show()
        self.area_end.show()
        self.btn_save.show()
    
    def change(self):
        self.clear()
        self.save_mod = 'change'
        print(self.save_mod)
        self.text_change.show()
        self.area_task_list.show()
        self.area_task_num.show()
        self.btn_take.show()
        self.tasks_get()
        self.area_task_list.clear()
        for task in self.tasks:
            self.area_task_list.appendPlainText(f'{task[0]}. {task[1]} {task[2]}-{task[3]}')
    
    def delete(self):
        self.clear()
        self.save_mod = 'delete'
        self.text_delete.show()
        self.area_task_list.show()
        self.area_task_num.show()
        self.btn_take.show()
        self.tasks_get()
        self.area_task_list.clear()
        for task in self.tasks:
            self.area_task_list.appendPlainText(f'{task[0]}. {task[1]} {task[2]}-{task[3]}')
            
    def delete_everything(self):
        pass
    
    def output(self):
        self.clear()
        self.text_output.show()
        self.text_type.show()
        self.radio_gante.show()
        self.radio_list.show()
        self.btn_type_get.show()
    
    def time_else(self):
        self.clear()
        self.start_db()
        self.birth_date = self.c.execute('SELECT Birth_date FROM Person').fetchall()[0][0].split('.')
        self.death_date = self.c.execute('SELECT Death_date FROM Person').fetchall()[0][0].split('.')
        self.end_db()
        burn_date = datetime(year=int(self.birth_date[0]), month=int(self.birth_date[2]), day=int(self.birth_date[1]))
        death_date = datetime(year=int(self.death_date[0]), month=int(self.death_date[2]), day=int(self.death_date[1]))
        today = datetime.now()
        days_until_death = (death_date - today).days
        days_burned = (today - burn_date).days
        self.text_else_days.setText(f'Вы прожили {abs(days_burned)} дней.')
        self.text_burn_days.setText(f'До смерти осталось {abs(days_until_death)} дней.')
        self.text_burn_days.show()
        self.text_else_days.show()
    
    def settings(self):
        self.clear()
        self.save_mod = 'settings'
        self.area_burthdate.show()
        self.area_deathdate.show()
        self.text_death.show()
        self.text_burth.show()
        self.btn_save.show()
        self.text_theme.show()
        self.radio_dark.show()
        self.radio_light.show()
        self.btn_delete_everything.show()
        
    def back(self):
        self.clear()
        if self.save_mod == 'change':
            self.change()
    
    def save(self):
        self.name = self.area_name.text()
        self.start = self.area_start.text()
        self.end = self.area_end.text()
        if self.save_mod == 'settings':
           self.text_settings_complete.show()
        elif self.name == '':
            self.text_name_err.show()
            self.text_date_err.hide()
            self.text_complete.hide()
        elif (len(self.start) == len(self.end) == 5) and (''.join(self.start.split('.')).isdigit() and ''.join(self.end.split('.')).isdigit()):
            if self.save_mod == 'create':
                self.tasks_get()
                print('create')
                # проверка копии (надо добавить)
                self.start_db()
                self.c.execute('INSERT INTO Tasks VALUES (?, ?, ?, ?)', (len(self.tasks)+1, self.name, self.start, self.end)).fetchall()
                self.end_db()
                self.text_name_err.hide()
                self.text_date_err.hide()
                self.text_complete.show()
                self.tasks_get()
            elif self.save_mod == 'change':
                print('change')
                # проверка копии (надо добавить)
                self.start_db()
                self.c.execute('UPDATE Tasks SET Name = ?, Start = ?, End = ? WHERE id = ?', (self.name, self.start, self.end, self.task_num)).fetchall()
                self.end_db()
                self.text_name_err.hide()
                self.text_date_err.hide()
                self.text_complete.show()
                self.tasks_get()
        else:
            self.text_name_err.hide()
            self.text_date_err.show()
            self.text_complete.hide()
            
    def take(self):
        self.task_num = self.area_task_num.text()
        if self.task_num != '':
            if self.save_mod == 'change':
                self.clear()  
                self.text_change.show()
                self.area_name.show()
                self.area_start.show()
                self.area_end.show()
                self.btn_save.show()
                self.btn_back.show()
            elif self.save_mod == 'delete':
                self.tasks_get()
                print(self.tasks[int(self.task_num)-1][0], type(self.tasks[int(self.task_num)-1][0]))
                self.start_db()
                self.c.execute('DELETE FROM Tasks WHERE id = ?', (self.tasks[int(self.task_num)-1][0],)).fetchall()
                for task in self.tasks[int(self.task_num)-1:]:
                    self.c.execute('UPDATE Tasks SET id = ? WHERE Name = ?', (int(task[0])-1, task[1])).fetchall()
                self.end_db()
                self.text.complete.show()
                
    def gante(self):
        # ось у
        groups = [task[1] for task in self.tasks]
        # ось х
        self.start_db()
        self.dates_beta = self.c.execute('SELECT Start, End FROM Tasks').fetchall()
        self.end_db()
        for date in self.dates_beta:
            self.dates.append(date[0])
            self.dates.append(date[1])
        map(lambda time: datetime.strptime(time, "%m-%d").date(), self.dates)
        
        counts = np.random.randint(2, 10, len(groups))
        plt.barh(groups, counts)
        plt.show()
    
    def tasks_list(self):
        with open('total_tasks.txt', 'w', encoding='utf-8') as file:
            file.write('')
        with open('total_tasks.txt', 'a', encoding='utf-8') as file:
            for task in self.tasks:
                file.write(f'{task[0]}. {task[1]} {task[2]}-{task[3]}\n')
        os.system('total_tasks.txt')
    
    def radio_change(self):
        radio_button = self.sender()
        if radio_button.isChecked():
            self.type = radio_button.text()
                
    def show_type(self):
        if self.type == '':
            self.text_type_err.show()
        else:
            self.text_type_err.hide()
            self.tasks_get()
            if self.type == 'Диаграмма Ганта':
                self.gante()
            elif self.type == 'Список дел':
                self.tasks_list()
    
    def clear(self):
        self.text_create.hide()
        self.text_change.hide()
        self.text_delete.hide()
        self.text_output.hide()
        self.text_settings.hide()
        self.text_type.hide()
        self.text_life.hide()
        self.text_else_days.hide()
        self.text_burn_days.hide()
        self.text_death.hide()
        self.text_burth.hide()
        self.text_theme.hide()
        
        self.text_complete.hide()
        self.text_settings_complete.hide()
        
        self.text_name_err.hide()
        self.text_date_err.hide()
        self.text_num_err.hide()
        self.text_copy_err.hide()
        self.text_type_err.hide()
        
        self.radio_gante.hide()
        self.radio_list.hide()
        self.radio_dark.hide()
        self.radio_light.hide()
        
        self.area_name.hide()
        self.area_start.hide()
        self.area_end.hide()
        self.area_burthdate.hide()
        self.area_deathdate.hide()
        
        self.area_task_num.hide()
        self.area_task_list.hide()
        
        self.btn_back.hide()
        self.btn_save.hide()
        self.btn_take.hide()
        self.btn_type_get.hide()
        self.btn_delete_everything.hide()
    

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    ex.clear()
    sys.exit(app.exec())

if __name__ == '__main__':
    main()
