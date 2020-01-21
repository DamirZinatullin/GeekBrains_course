# Задание-1:
# Реализуйте описаную ниже задачу, используя парадигмы ООП:
# В школе есть Классы(5А, 7Б и т.д.), в которых учатся Ученики.
# У каждого ученика есть два Родителя(мама и папа).
# Также в школе преподают Учителя. Один учитель может преподавать
# в неограниченном кол-ве классов свой определенный предмет.
# Т.е. Учитель Иванов может преподавать математику у 5А и 6Б,
# но больше математику не может преподавать никто другой.

# Выбранная и заполненная данными структура должна решать следующие задачи:
# 1. Получить полный список всех классов школы
# 2. Получить список всех учеников в указанном классе
#  (каждый ученик отображается в формате "Фамилия И.О.")
# 3. Получить список всех предметов указанного ученика
#  (Ученик --> Класс --> Учителя --> Предметы)
# 4. Узнать ФИО родителей указанного ученика
# 5. Получить список всех Учителей, преподающих в указанном классе

# students = [
#            Student(), .....
#            ]
#
# teechers = [
#            Teacher(..), ....
#            ]
#
# School(...., students, teechers)


class School:
    def __init__(self, school_name: str, school_adress: list, teachers: list,
                 students: list):
        self._school_name = school_name
        self._school_adress = school_adress
        self._teachers = teachers  # список объектов Teacher
        self._students = students  # список объектов Student


class People:
    def __init__(self, last_name: str, first_name: str, middle_name: str):
        self._last_name = last_name
        self._first_name = first_name
        self._middle_name = middle_name

    def __str__(self):
        return '%s %s %s' % (
            self._last_name, self._first_name, self._middle_name)


class Student(People):
    def __init__(self, last_name, first_name, middle_name,
                 class_room, mother, father):
        super(Student, self).__init__(last_name, first_name, middle_name)
        self._class_room = class_room
        self._parents = {
            'mother': mother,
            'father': father,
        }

    def __str__(self):
        return '%s %s. %s.' % (
            self._last_name, self._first_name[0], self._middle_name[0])

    def parents(self):
        return 'Родители студента %s\n Мать: %s\n Отец: %s' % (
            self, self._parents['mother'], self._parents['father'])


class Teacher(People):
    def __init__(self, last_name, first_name, middle_name, courses, classes):
        super(Teacher, self).__init__(last_name, first_name, middle_name)
        self._courses = courses
        self._classes = classes


def list_of_classes(stud: Student):
    list_of_class = []
    for el in stud:
        list_of_class.append(el._class_room)
    return sorted(list_of_class)


def list_of_students_in_class(class_name: str):
    print('Список учеников класса %s:' % class_name)
    cls_list = []
    for el in students_1:
        if el._class_room == class_name:
            cls_list.append(el)
    return cls_list


def list_of_subjects(stud: Student):
    print('Список предметов студента', stud)
    lst_of_subjects_of_student = []
    for el in teachers_1:
        if stud._class_room in el._classes:
            lst_of_subjects_of_student.append(el._courses)
    return lst_of_subjects_of_student


def teachers_of_class(class_name: str):
    print('\nУчителя класса', class_name)
    list_of_teachers = []
    for el in teachers_1:
        if class_name in el._classes:
            list_of_teachers.append(el)
    return list_of_teachers


mother_of_vasya = People('Иванова', 'Вера', 'Павловна')
father_of_vasya = People('Иванов', 'Петр', 'Игоревич')
mother_of_petya = People('Сидорова', 'Мария', 'Михайловна')
father_of_petya = People('Сидоров', 'Игорь', 'Валерьевич')
mother_of_sasha = People('Колесова', 'Валентина', 'Геннадиевна')
father_of_sasha = People('Колесов', 'Семен', 'Витальевич')
vasya = Student('Иванов', 'Василий', 'Петрович', '5А', mother_of_vasya,
                father_of_vasya)
petya = Student('Сидоров', 'Петр', 'Игоревич', '10Г', mother_of_petya,
                father_of_petya)
sasha = Student('Колесова', 'Александра', 'Семеновна', '10Г', mother_of_sasha,
                father_of_sasha)
nadezhda = Teacher('Аникина', 'Надежда', 'Петровна', 'обществознание',
                   ['5А', '5Б', '10Г'])
tatyana = Teacher('Петрова', 'Татьяна', 'Викторовна', 'математика', ['6А'])

students_1 = [vasya, petya, sasha]
teachers_1 = [nadezhda, tatyana]
school = School('131', 'Гагарина 50', teachers_1, students_1)

print('Список классов школы:', '\n', list_of_classes(students_1), '\n')

for el in list_of_students_in_class('10Г'):
    print(el)

print('\n', vasya.parents(), '\n')

print(list_of_subjects(vasya), '\n')

print(vasya.parents())

for el in teachers_of_class('5А'):
    print(el)
