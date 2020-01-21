# Задание-1: Решите задачу (дублированную ниже):

# Дана ведомость расчета заработной платы (файл "data/workers").
# Рассчитайте зарплату всех работников, зная что они получат полный оклад,
# если отработают норму часов. Если же они отработали меньше нормы,
# то их ЗП уменьшается пропорционально, а за заждый час переработки они
# получают
# удвоенную ЗП, пропорциональную норме.
# Кол-во часов, которые были отработаны, указаны в файле "data/hours_of"

# С использованием классов.
# Реализуйте классы сотрудников так, чтобы на вход функции-конструктора
# каждый работник получал строку из файла

import re
import os


class Person:
    def __init__(self, str_of_worker: str):
        worker = re.findall(r'\w+', str_of_worker)
        self.worker_str = str(worker)
        self.name = worker[0]
        self.last_name = worker[1]
        self.salary = int(worker[2])
        self.position = worker[3]
        self.norm_of_hours = int(worker[4])

    def __str__(self):
        return self.name + ' ' + self.last_name

    def pay(self, hours):
        if hours == self.norm_of_hours:
            pay = self.salary
        elif hours > self.norm_of_hours:
            pay = (self.salary + (hours - self.norm_of_hours) * self.salary
                   / self.norm_of_hours * 2)
        else:
            pay = hours / self.norm_of_hours * self.salary
        return ': %d' % pay

    def hours_of(self, path):
        hours_of_file = open(path, 'r', encoding='UTF-8')
        hours_of_list = []
        for el in hours_of_file:
            hours_of_list.append(re.findall(r'\w+', el))
        hours_of_file.close()
        for el in hours_of_list:
            if el[0] == self.name and el[1] == self.last_name:
                worked = el[-1]
        return worked


path = os.path.join('data', 'workers.txt')
workers_file = open(path, 'r', encoding='UTF-8')
head_of_data = workers_file.readline()
workers_list = []
for el in workers_file:
    workers_list.append(Person(el))
workers_file.close()

path_hours_of_file = os.path.join('data', 'hours_of.txt')
for el in workers_list:
    print(el, el.pay(int(el.hours_of(path_hours_of_file))))
