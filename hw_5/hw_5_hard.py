# Задание-1:
# Доработайте реализацию программы из примера examples/5_with_args.py,
# добавив реализацию следующих команд (переданных в качестве аргументов):
#   cp <file_name> - создает копию указанного файла
#   rm <file_name> - удаляет указанный файл (запросить подтверждение операции)
#   ls - отображение полного пути текущей директории
# путь считать абсолютным (full_path) -
# в Linux начинается с /, в Windows с имени диска,
# все остальные пути считать относительными.

# Важно! Все операции должны выполняться в той директории, в который вы
# находитесь.
# Исходной директорией считать ту, в которой был запущен скрипт.

# P.S. По возможности, сделайте кросс-платформенную реализацию.


# Данный скрипт можно запускать с параметрами:
# python with_args.py param1 param2 param3
import os
import sys
import shutil

print('sys.argv = ', sys.argv)


def print_help():
    print("help - получение справки")
    print("mkdir <dir_name> - создание директории")
    print('cp <file_name> - создает копию указанного файла')
    print('ls - отображение полного пути текущей директории')
    print('rm <file_name> - удаляет указанный файл')


def make_dir():
    if not dir_name:
        print("Необходимо указать имя директории вторым параметром")
        return
    dir_path = os.path.join(os.getcwd(), dir_name)
    try:
        os.mkdir(dir_path)
        print('директория {} создана'.format(dir_name))
    except FileExistsError:
        print('директория {} уже существует'.format(dir_name))


def cp():
    path_of_file = os.path.join(os.getcwd(), file_name)
    shutil.copyfile(path_of_file, os.path.join(os.getcwd(), 'copy_of_' +
                                               file_name))
    print('Файл {} скопрован'.format(file_name))


def ls():
    print('Полный путь текущей директории', os.getcwd())


def rm():
    if file_name is not None:
        path_of_file = os.path.join(os.getcwd(), file_name)
        if os.path.exists(path_of_file):
            confirm = input("Подвердите удаление файла {}\n Введите Y для"
                            " удаления файла, введите любой другой символ для "
                            "отмены удаления\n".format(file_name))
            if confirm == 'Y':
                os.remove(path_of_file)
                print('Файл {} удален'.format(file_name))
            else:
                pass
        else:
            print('Такого файла не существует')
    if dir_name is not None:
        path_of_dir = os.path.join(os.getcwd(), dir_name)
        if os.path.exists(path_of_dir):
            confirm = input("Подвердите удаление папки {}\n Введите Y для "
                            "удаления файла,введите любой другой символ для "
                            "отмены удаления\n".format(dir_name))
            if confirm == 'Y':
                shutil.rmtree(path_of_dir)
                print('Папка {} удалена'.format(dir_name))
            else:
                pass
        else:
            print('Такой папки не существует')


do = {
    "help": print_help,
    "mkdir": make_dir,
    "cp": cp,
    "rm": rm,
    'ls': ls
}

try:
    if '.' not in sys.argv[2]:
        dir_name = sys.argv[2]
        file_name = None
    else:
        file_name = sys.argv[2]
        dir_name = None
except IndexError:
    dir_name = None
    file_name = None
try:
    key = sys.argv[1]
except IndexError:
    key = None

if key:
    if do.get(key):
        do[key]()
    else:
        print("Задан неверный ключ\nУкажите ключ help для получения справки")
