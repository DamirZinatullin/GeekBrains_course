import os
import sys
import shutil


# Задача-1:
# Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
# из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.


def make_dir():
    if not dir_name:
        print("Необходимо указать имя директории вторым параметром")
    try:
        new_dir_path = os.path.join(os.getcwd(), dir_name)
        os.mkdir(new_dir_path)
        print('Директория {} cоздана'.format(dir_name))
    except FileExistsError:
        print('Директория {} уже существует'.format(dir_name))


def del_dir():
    if not dir_name:
        print("Необходимо указать имя директории вторым параметром")
    try:
        del_dir_path = os.path.join(os.getcwd(), dir_name)
        os.rmdir(del_dir_path)
        print('Директория {} удалена'.format(dir_name))
    except FileNotFoundError:
        print('Директории {} не существует'.format(dir_name))


def list_of_dir():

    return os.listdir(dir_path)


if __name__ == "__main__":
    for num_of_dir in range(1, 10):
        dir_name = 'dir_%d' % num_of_dir
        dir_path = os.path.join(os.getcwd(), dir_name)
        make_dir()
    for num_of_dir in range(1, 10):
        dir_name = 'dir_%d' % num_of_dir
        dir_path = os.path.join(os.getcwd(), dir_name)
        del_dir()

# Задача-2:
# Напишите скрипт, отображающий папки текущей директории.


if __name__ == "__main__":
    dir_path = os.getcwd()
    list_of_directories = [el for el in list_of_dir() if '.' not in el]
    print("\nСписок папок в текущей директории:", list_of_directories)

# Задача-3:
# Напишите скрипт, создающий копию файла, из которого запущен данный скрипт.
if __name__ == "__main__":
    shutil.copyfile(sys.argv[0], os.path.join(os.getcwd(), 'copied_file.py'))
