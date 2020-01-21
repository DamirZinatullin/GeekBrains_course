# Задача-1: Написать класс для фигуры-треугольника, заданного координатами
# трех точек.
# Определить методы, позволяющие вычислить: площадь, высоту и периметр фигуры.
import math


class Side:
    @staticmethod
    def side(x, y):
        return math.sqrt((x[0] - y[0]) ** 2 + (x[1] - y[1]) ** 2)


class Triangle(Side):
    def __init__(self, a: tuple, b: tuple, c: tuple):
        if self.side(a, b) + self.side(b, c) != (self.side(c, a) and
                                                 self.side(b, c) +
                                                 self.side(c, a) !=
                                                 self.side(a, b)):
            self._a = a
            self._b = b
            self._c = c
            self.ab = self.side(a, b)
            self.bc = self.side(b, c)
            self.ca = self.side(c, a)
        else:
            print('Это не треугольник, точки образуют прямую')
            return None

    def perimetr(self) -> float:
        try:
            p = self.ab + self.bc + self.ca
            return f'Периметр треугольника: {p}'
        except AttributeError:
            return 'Это не треугольник, периметр не посчитан'

    def area(self):
        """
        Площадь по формуле Герона
        """
        try:
            polusum = sum((self.ab, self.bc, self.ca)) / 2
            self.s = math.sqrt(polusum * (polusum - self.ab) *
                               (polusum - self.bc) * (polusum - self.ca)
                               )
            return f'Площадь треугольника {self.s}'
        except AttributeError:
            return 'Это не треугольник, площадь не посчитана'

    def heigh(self, str_of_side: str):
        try:
            if str_of_side is 'ab' or str_of_side is 'ba':
                h = self.s * 2 / self.ab
            elif str_of_side is 'bc' or str_of_side is 'cb':
                h = self.s * 2 / self.bc
            elif str_of_side is 'ca' or str_of_side is 'ac':
                h = self.s * 2 / self.ca
            else:
                print('Неправильное основание')
                h = None
            return f'Высота трегольника по основанию {str_of_side}: {h}'
        except AttributeError:
            return 'Это не треугольник, высота не посчитана'


triang = Triangle((0, 0), (5, 6), (5, 0))
print(triang.perimetr())
print(triang.area())
print(triang.heigh('ba'), '\n')


# Задача-2: Написать Класс "Равнобочная трапеция", заданной координатами 4-х
# точек.
# Предусмотреть в классе методы:
# проверка, является ли фигура равнобочной трапецией;
# вычисления: длины сторон, периметр, площадь.


class Trapeze(Triangle):
    def __init__(self, a, b, c, d):
        super(Trapeze, self).__init__(a, b, c)
        self._d = d
        self.bd = self.side(b, d)
        self.cd = self.side(c, d)
        self.da = self.side(d, a)
        if self.check():
            print('Это равнобокая трапеция')
        else:
            print('Фигура не является равнобокой трапецией')

    def check(self) -> bool:

        """Проверка на равнобочность трапеции"""

        check_trap = False
        try:
            k_1 = (self._b[1] - self._a[1]) / (self._b[0] - self._a[0])
        except ZeroDivisionError:
            k_1 = math.inf
        try:
            k_2 = (self._c[1] - self._b[1]) / (self._c[0] - self._b[0])
        except ZeroDivisionError:
            k_2 = math.inf
        try:
            k_3 = (self._d[1] - self._c[1]) / (self._d[0] - self._c[0])
        except ZeroDivisionError:
            k_3 = math.inf
        try:
            k_4 = (self._a[1] - self._d[1]) / (self._a[0] - self._d[0])
        except ZeroDivisionError:
            k_4 = math.inf
        try:
            k_5 = (self._a[1] - self._c[1]) / (self._a[0] - self._c[0])
        except ZeroDivisionError:
            k_5 = math.inf
        try:
            k_6 = (self._d[1] - self._b[1]) / (self._d[0] - self._b[0])
        except ZeroDivisionError:
            k_6 = math.inf
        if k_1 == k_3 and (k_2 != k_4, k_5, k_6) and (self.bc == self.da):
            check_trap = True
            self.osn_1 = self.ab  # Основание трапеции 1
            self.osn_2 = self.cd  # Основание трапеции 2
            self.bok = min(self.bc, self.bd)
        elif k_2 == k_4 and (k_1 != k_3, k_5, k_6) and (self.ab == self.cd):
            check_trap = True
            self.osn_1 = self.bc
            self.osn_2 = self.da
            self.bok = min(self.ab, self.ca)
        elif k_5 == k_6 and (k_2 != k_4, k_1, k_3) and (self.bc == self.da):
            check_trap = True
            self.osn_1 = self.ca  # Основание трапеции 1
            self.osn_2 = self.bd  # Основание трапеции 2
            self.bok = min(self.bc, self.ab)
        elif k_2 == k_4 and (k_2 != k_4, k_1, k_3) and (self.ca == self.bd):
            check_trap = True
            self.osn_1 = self.bc  # Основание трапеции 1
            self.osn_2 = self.da  # Основание трапеции 2
            self.bok = min(self.ca, self.cd)
        return check_trap

    def perimetr(self):
        if self.check():
            return sum((self.osn_1, self.osn_2, 2 * self.bok))
        else:
            print('Это не равнобокая трапеция, периметр не посчитан')

    def area(self):
        if self.check():
            self.s = (self.osn_1 + self.osn_2) / 2 * math.sqrt(
                (self.bok) ** 2 - ((self.osn_1 - self.osn_2) ** 2) / 4)
        else:
            print('Фигура не является равнобокой трапецией')
            self.s = None
        return self.s


trap = Trapeze((4, 3), (5, 0), (1, 4), (0, 0))
print('Периметр фигуры:', trap.perimetr())
print('Площадь равнобокой трапеции:', trap.area())
