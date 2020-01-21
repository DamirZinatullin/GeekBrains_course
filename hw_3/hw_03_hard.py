from typing import Optional, Dict, List, Set
# Задание-1:
# Написать программу, выполняющую операции (сложение и вычитание) с простыми
# дробями.
# Дроби вводятся и выводятся в формате:
# n x/y ,где n - целая часть, x - числитель, у - знаменатель.
# Дроби могут быть отрицательные и не иметь целой части, или иметь только целую
# часть.
# Примеры:
# Ввод: 5/6 + 4/7 (всё выражение вводится целиком в виде строки)
# Вывод: 1 17/42  (результат обязательно упростить и выделить целую часть)
# Ввод: -2/3 - -2
# Вывод: 1 1/3

import os

from fractions import Fraction


def int_and_frac(num: str) -> Fraction:
    if " " in num:  # Если число имеет целую и дробную части
        num_int = int(num[:num.index(' ')])  # Целая часть первого числа
        num_frac = Fraction(num[num.index(' ') + 1:])  # Дробная часть первого
        # числа
    else:
        try:
            num_int = int(num)
            num_frac = 0
        except ValueError:
            num_int = 0
            num_frac = Fraction(num)
    if num_int < 0:
        num_frac = - num_frac
    return num_int, num_frac


math_of_fractions = '-5/4 - 2 1/10'
summir = False  # распознователь операции над дробями
for i in range(len(math_of_fractions)):  # Распознование части строки с числом
    if math_of_fractions[i] == "+" or math_of_fractions[i] == "-":
        if math_of_fractions[i + 1] == " " and math_of_fractions[i - 1] == " ":
            if math_of_fractions[i] == "+":
                summir = True
            a = math_of_fractions[:i - 1]
            b = math_of_fractions[i + 2:]
a_int = int_and_frac(a)[0]
a_frac = int_and_frac(a)[1]
b_int = int_and_frac(b)[0]
b_frac = int_and_frac(b)[1]
if summir:
    math_of_frac = a_int + b_int + a_frac + b_frac
else:
    math_of_frac = a_int - b_int + a_frac - b_frac
if math_of_frac - int(math_of_frac) == 0:
    print(math_of_frac)
else:
    print(int(math_of_frac), abs(math_of_frac - int(math_of_frac)))

# Задание-2:
# Дана ведомость расчета заработной платы (файл "data/workers").
# Рассчитайте зарплату всех работников, зная что они получат полный оклад,
# если отработают норму часов. Если же они отработали меньше нормы,
# то их ЗП уменьшается пропорционально, а за заждый час переработки
# они получают удвоенную ЗП, пропорциональную норме.
# Кол-во часов, которые были отработаны, указаны в файле "data/hours_of"

path = os.path.join('data', 'workers.txt')
path_of_hours = os.path.join('data', 'hours_of.txt')
with open(path, 'r', encoding='UTF-8') as f:
    data_head = f.readline()
    data = f.readlines()
with open(path_of_hours, 'r', encoding='UTF-8') as g:
    data_of_hours_head = g.readline()
    data_of_hours = g.readlines()
i_name = data_head.find("Имя")
i_surname = data_head.find("Фамилия")
i_salary = data_head.find("Зарплата")
i_position = data_head.find("Должность")
i_hours_norm = data_head.find("Норма_часов")
for line in data:
    full_name = line[i_name:line.find(" ", i_surname)]
    norm_of_hours = int(line[line.rfind(' '):])
    salary = int(line[i_salary:line.find(" ", i_salary)])
    for line_of_hours in data_of_hours:f
        hours_of_working = int(line_of_hours[line_of_hours.rfind(' '):])
        if full_name in line_of_hours:
            if hours_of_working == norm_of_hours:
                pay_to_worker = salary
                print(full_name + "   Выплата:  " + str(pay_to_worker))
            elif hours_of_working < norm_of_hours:
                pay_to_worker = hours_of_working / norm_of_hours * salary
                print(full_name + "   Выплата:  " + str(pay_to_worker))
            else:
                pay_to_worker = salary + hours_of_working % \
                                norm_of_hours * salary / norm_of_hours * 2
                print(full_name + "   Выплата:  " + str(pay_to_worker))

# Задание-3:
# Дан файл ("data/fruits") со списком фруктов.
# Записать в новые файлы все фрукты, начинающиеся с определенной буквы.
# Т.е. в одном файле будут все фрукты на букву “А”, во втором на “Б” и т.д.
# Файлы назвать соответственно.
# Пример имен файлов: fruits_А, fruits_Б, fruits_В ….
# Важно! Обратите внимание, что нет фруктов, начинающихся с некоторых букв.
# Напишите универсальный код, который будет работать с любым списком фруктов
# и распределять по файлам в зависимости от первых букв, имеющихся в списке
# фруктов.
# Подсказка:
# Чтобы получить список больших букв русского алфавита:
# print(list(map(chr, range(ord('А'), ord('Я')+1))))
path = os.path.join('data', 'fruits.txt')
alphabet = list(map(chr, range(ord('А'), ord('Я') + 1)))
for letter in alphabet:
    name_of_file = "fruits_" + letter + ".txt"
    path_to_sorted_file = os.path.join('data', name_of_file)
    with open(path, 'r', encoding="UTF-8") as f:
        for line in f:
            if line[0] == letter:
                with open(path_to_sorted_file, 'a', encoding='UTF-8') as g:
                    g.write(line)
