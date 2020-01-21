# Задача-1:
# Напишите небольшую консольную утилиту,
# позволяющую работать с папками текущей директории.
# Утилита должна иметь меню выбора действия, в котором будут пункты:
# 1. Перейти в папку
# 2. Просмотреть содержимое текущей папки
# 3. Удалить папку
# 4. Создать папку
# При выборе пунктов 1, 3, 4 программа запрашивает название папки
# и выводит результат действия: "Успешно создано/удалено/перешел",
# "Невозможно создать/удалить/перейти"

# Для решения данной задачи используйте алгоритмы из задания easy,
# оформленные в виде соответствующих функций,
# и импортированные в данный файл из easy.py
import os
import sys

import hw_5_easy as my_module


def print_help():
    print('Справка:')
    print("mkdir <dir_name> - Создание папки с именем <dir_name>")
    print("dldir <dir_name> - Удаление папки с именем <dir_name>")
    print("chdir <dir_name> - Переход в директорию с именем <dir_name>")
    print("updir - Переход в директорию уровнем выше")
    print("lsdir - Вывести содержимое текущей директории \n")


def change_dir():
    os.chdir(my_module.dir_path)
    f = open(path_to_init_file, 'w', encoding='UTF-8')
    f.write(my_module.dir_path)
    print('Произведен переход в директорию', my_module.dir_name)
    print('os.getcwd:', my_module.dir_path)
    f.close()


def up_dir():
    global f
    f = open(path_to_init_file, 'r', encoding='UTF-8')
    my_module.dir_path = f.readline()
    os.chdir(os.path.split(my_module.dir_path)[0])
    f.close()
    f = open(path_to_init_file, 'w', encoding='UTF-8')
    f.write(os.getcwd())
    f.close()
    print(os.getcwd())


root_dir = os.getcwd()
path_to_init_file = os.path.join(root_dir, 'current_dir.txt')
try:
    f = open(path_to_init_file, 'r', encoding='UTF-8')
    path_to_current_dir = f.readline()
    f.close()
except FileNotFoundError:
    f = open(path_to_init_file, 'w', encoding='UTF-8')
    path_to_current_dir = os.getcwd()
    f.write(path_to_current_dir)
    f.close()

do = {
    "help": print_help,
    "mkdir": my_module.make_dir,
    "dldir": my_module.del_dir,
    "lsdir": my_module.list_of_dir,
    "chdir": change_dir,
    "updir": up_dir}
do["help"]()

try:
    my_module.dir_name = sys.argv[2]
    my_module.dir_path = os.path.join(path_to_current_dir, my_module.dir_name)
except IndexError:
    my_module.dir_name = None
try:
    key = sys.argv[1]
except IndexError:
    key = None
if key:
    if do.get(key):
        if key == "lsdir":
            try:
                f = open(path_to_init_file, 'r', encoding='UTF-8')
                my_module.dir_path = f.readline()
                f.close()
            except FileExistsError:
                my_module.dir_path = os.getcwd()
            print('os.getcwd:', my_module.dir_path)
            print('Содержимое текущей директории:\n', do[key]())
        else:
            do[key]()
    else:
        print("Введен неправильный ключ")
