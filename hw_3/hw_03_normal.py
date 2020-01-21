from typing import Union, Optional, Dict, List, Set
import math


# Задание-1:
# Напишите функцию, возвращающую ряд Фибоначчи с n-элемента до m-элемента.
# Первыми элементами ряда считать цифры 1 1

def fibonacci(n: int, m: int) -> List:
    list_of_fibonacci = [1, 1]
    i = 1
    while i < (m - 1):
        list_of_fibonacci.append(list_of_fibonacci[i] +
                                 list_of_fibonacci[(i - 1)])
        i += 1
    return list_of_fibonacci[(n - 1):(m + 1)]


print(fibonacci(3, 6))


# Задача-2:
# Напишите функцию, сортирующую принимаемый список по возрастанию.
# Для сортировки используйте любой алгоритм (например пузырьковый).
# Для решения данной задачи нельзя использовать встроенную функцию и метод
# sort()


def sort_to_max(origin_list: List) -> List:
    len_of_origin_list = len(origin_list)
    for i in range(len_of_origin_list - 2):
        for j in range(len_of_origin_list - i - 1):
            if origin_list[j] > origin_list[j + 1]:
                origin_list[j], origin_list[j + 1] = origin_list[j + 1], \
                                                     origin_list[j]
            else:
                continue
    return origin_list


print(sort_to_max([2, 6, -2, -12, 2.5, 20, -11, 4, 4, 0]))


# Задача-3:
# Напишите собственную реализацию стандартной функции filter.4
# Разумеется, внутри нельзя использовать саму функцию filter.
def my_filter(func, seq):
    if func is None:
        return [x for x in seq if x]
    return [x for x in seq if func(x)]


print('\nЗадача 3')
print(list(my_filter(lambda x: x > 0, [-5, 4, -3, -2, 4, 3])))

# # Задача-4:
# Даны четыре точки А1(х1, у1), А2(x2 ,у2), А3(x3 , у3), А4(х4, у4).
# Определить, будут ли они вершинами параллелограмма.
d = {"А1": [1, -2], "А2": [-1, 1], "А3": [2, 1], "А4": [-1, -2]}  # создание
# словаря с координатами точек
x_1, y_1 = d["А1"]
x_2, y_2 = d["А2"]
x_3, y_3 = d["А3"]
x_4, y_4 = d["А4"]
try:
    k2_1 = (y_2 - y_1) / (x_2 - x_1)
except ZeroDivisionError:
    k2_1 = "vert"
try:
    k3_1 = (y_3 - y_1) / (x_3 - x_1)
except ZeroDivisionError:
    k3_1 = "vert"
try:
    k4_1 = (y_4 - y_1) / (x_4 - x_1)
except ZeroDivisionError:
    k4_1 = "vert"
try:
    k3_2 = (y_3 - y_2) / (x_3 - x_2)
except ZeroDivisionError:
    k3_2 = "vert"
try:
    k4_2 = (y_4 - y_2) / (x_4 - x_2)
except ZeroDivisionError:
    k4_2 = "vert"
if k3_2 == k4_1 and math.sqrt((y_3 - y_2) ** 2 + (x_3 - x_2) ** 2) == \
        math.sqrt((y_4 - y_1) ** 2 + (x_4 - x_1) ** 2):
    print("Это параллелограмм")
elif k4_2 == k3_1 and math.sqrt((y_4 - y_2) ** 2 + (x_4 - x_2) ** 2) == \
        math.sqrt((y_3 - y_1) ** 2 + (x_3 - x_1) ** 2):
    print("Это параллелограмм")
else:
    print("Это не параллелограмм")
