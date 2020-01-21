#!/usr/bin/python3

"""
== Лото ==

Правила игры в лото.

Игра ведется с помощью специальных карточек, на которых отмечены числа,
и фишек (бочонков) с цифрами.

Количество бочонков — 90 штук (с цифрами от 1 до 90).
Каждая карточка содержит 3 строки по 9 клеток. В каждой строке по 5 случайных цифр,
расположенных по возрастанию. Все цифры в карточке уникальны. Пример карточки:

--------------------------
    9 43 62          74 90
 2    27    75 78    82
   41 56 63     76      86
--------------------------

В игре 2 игрока: пользователь и компьютер. Каждому в начале выдается
случайная карточка.

Каждый ход выбирается один случайный бочонок и выводится на экран.
Также выводятся карточка игрока и карточка компьютера.

Пользователю предлагается зачеркнуть цифру на карточке или продолжить.
Если игрок выбрал "зачеркнуть":
	Если цифра есть на карточке - она зачеркивается и игра продолжается.
	Если цифры на карточке нет - игрок проигрывает и игра завершается.
Если игрок выбрал "продолжить":
	Если цифра есть на карточке - игрок проигрывает и игра завершается.
	Если цифры на карточке нет - игра продолжается.

Побеждает тот, кто первый закроет все числа на своей карточке.

Пример одного хода:

Новый бочонок: 70 (осталось 76)
------ Ваша карточка -----
 6  7          49    57 58
   14 26     -    78    85
23 33    38    48    71
--------------------------
-- Карточка компьютера ---
 7 87     - 14    11
      16 49    55 88    77
   15 20     -       76  -
--------------------------
Зачеркнуть цифру? (y/n)

Подсказка: каждый следующий случайный бочонок из мешка удобно получать
с помощью функции-генератора.

Подсказка: для работы с псевдослучайными числами удобно использовать
модуль random: http://docs.python.org/3/library/random.html

"""

import random
import re


class IterObj:
    """
    Объект итератор
    """

    def __init__(self, start=0, stop=91):
        self.start = start
        self.stop = stop

    # Объект считается итератором - если у него есть метод __next__

    def __next__(self):
        self.i += 1
        if self.i <= self.stop:
            return self.i
        else:
            raise StopIteration


class Ticket:
    def __init__(self, lines=3, columns=9, skips=4):
        self.lines = lines
        self.columns = columns
        self.skips = skips
        list_of_nums = random.sample(range(1, 91),
                                     self.lines * (self.columns - self.skips))
        ticket = []
        column = 0
        amount_of_skips = 0
        for line in range(1, lines + 1):
            row = []
            while column < line * (columns - skips):
                row.append(list_of_nums[column])
                column += 1
            ticket.append(sorted(row))
        while amount_of_skips < self.skips:
            amount_of_skips += 1
            for line in ticket:
                skip = random.randint(0, len(line))
                line.insert(skip, 0)
        self.table = ticket

    def __str__(self):
        str_to_print = ''
        for line in self.table:
            for el in line:
                if el == 0:
                    str_to_print = str_to_print + '   '
                else:
                    str_to_print = str_to_print + (
                        ' {}'.format(
                            str(el) if len(str(el)) == 2 else '{} '.format(
                                str(el))))
            print(str_to_print)
            str_to_print = ''
        return ''

    def check_win(self):
        check_win = False
        crossed_out = 0
        for line in self.table:
            for el in line:
                if el == '-':
                    crossed_out += 1
        if crossed_out == self.columns * self.lines - self.lines * self.skips:
            check_win = True
        return check_win


class PlayerTicket(Ticket):
    def __init__(self, lines=3, columns=9, skips=4):
        Ticket.__init__(self, lines, columns, skips)

    def __str__(self):
        str_to_print = 'Ваша карточка'
        print('------ {} ------'.format(str_to_print))
        return Ticket.__str__(self)

    def next_step(self, num: int):
        num_in_ticket = False
        line_of_including = None
        column_of_including = None
        game_over = False
        input_str = input('зачеркнуть/продолжить  ')
        if input_str != 'зачеркнуть' and input_str != 'продолжить':
            input_str = input('зачеркнуть/продолжить  ')
        for line in self.table:
            if num in line:
                num_in_ticket = True
                line_of_including = self.table.index(line)
                column_of_including = line.index(num)
                pass
        if input_str == 'зачеркнуть':
            if num_in_ticket:
                self.table[line_of_including][column_of_including] = '-'
            else:
                game_over = True
        else:
            if num_in_ticket:
                game_over = True
        if game_over:
            print('Вы проиграли')
            return False
        else:
            print(self)
            return True


class ComputerTicket(Ticket):
    def __init__(self, lines=3, columns=9, skips=4):
        Ticket.__init__(self, lines, columns, skips)

    def __str__(self):
        str_to_print = 'Карточка компьютера'
        print('--- {} ---'.format(str_to_print))
        return Ticket.__str__(self)

    def next_step(self, num):
        num_in_ticket = False
        line_of_including = None
        column_of_including = None
        for line in self.table:
            if num in line:
                num_in_ticket = True
                line_of_including = self.table.index(line)
                column_of_including = line.index(num)
                pass
        if num_in_ticket:
            self.table[line_of_including][column_of_including] = '-'
        print(self)
        return num_in_ticket


rand_cask_list = random.sample(range(1, 91), 90)
player_ticket = PlayerTicket()
computer_ticket = ComputerTicket()
print(player_ticket)
print(computer_ticket)
for el in rand_cask_list:
    print('Новый бочонок:{} (осталось {})'.format(el, len(
        rand_cask_list) - rand_cask_list.index(el) - 1))
    if not player_ticket.next_step(el):
        break
    computer_ticket.next_step(el)
    if computer_ticket.check_win() and player_ticket.check_win():
        print('Ничья')
        break
    elif player_ticket.check_win():
        print('Вы выиграли')
        break
    elif computer_ticket.check_win():
        print('Выиграл компьюер')
        break
