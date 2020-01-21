# Задание-1:
# Напишите функцию, округляющую полученное произвольное десятичное число
# до кол-ва знаков (кол-во знаков передается вторым аргументом).
# Округление должно происходить по математическим правилам
# (0.6 --> 1, 0.4 --> 0). # Для решения задачи не используйте встроенные
# функции и функции из модуля math.


def my_round(number, ndigits):
    temp_number = number * (10 ** (ndigits + 1))
    if temp_number % 10 >= 4:
        temp_number += 10
    temp_number //= 10
    return int(temp_number) / (10 ** ndigits)


print(my_round(24.424524, 4))


# Задание-2:
# Дан шестизначный номер билета. Определить, является ли билет счастливым.
# Решение реализовать в виде функции.
# Билет считается счастливым, если сумма его первых и последних цифр равны.
# !!!P.S.: функция не должна НИЧЕГО print'ить

def lucky_ticket(ticket_number: int) -> bool:
    str_of_ticket_number = str(ticket_number)
    if sum([int(str_of_ticket_number[0]),
            int(str_of_ticket_number[1]),
            int(str_of_ticket_number[2])]) == sum(
        [int(str_of_ticket_number[-1]),
         int(str_of_ticket_number[-2]),
         int(str_of_ticket_number[-3])]):
        return True
    else:
        return False


res = lucky_ticket(624642)
print(res)
