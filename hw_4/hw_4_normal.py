import re
import os
import random

# Задание-1:
# Вывести символы в нижнем регистре, которые находятся вокруг
# 1 или более символов в верхнем регистре.
# Т.е. из строки "mtMmEZUOmcq" нужно получить ['mt', 'm', 'mcq']
# Решить задачу двумя способами: с помощью re и без.

line = 'mtMmEZUOmcqWiryMQhhTxqKdSTKCYEJlEZCsGAMkgAYEOmHBSQsSUHKvSfbmxULaysmNO' \
       'GIPHpEMujalpPLNzRWXfwHQqwksrFeipEUlTLeclMwAoktKlfUBJHPsnawvjPhfgewVzK' \
       'TUfSYtBydXaVIpxWjNKgXANvIoumesCSSvjEGRJosUfuhRRDUuTQwLlJJJDdkVjfSAHqn' \
       'LxooisBDWuxIhyjJaXDYwdoVPnsllMngNlmkpYOlqXEFIxPqqqgAWdJsOvqppOfyIVjXa' \
       'pzGOrfinzzsNMtBIOclwbfRzytmDgEFUzxvZGkdOaQYLVBfsGSAfJMchgBWAsGnBnWete' \
       'kUTVuPluKRMQsdelzBgLzuwiimqkFKpyQRzOUyHkXRkdyIEBvTjdByCfkVIAQaAbfCvzQ' \
       'WrMMsYpLtdqRltXPqcSMXJIvlBzKoQnSwPFkapxGqnZCVFfKRLUIGBLOwhchWCdJbRuXb' \
       'JrwTRNyAxDctszKjSnndaFkcBZmJZWjUeYMdevHhBJMBSShDqbjAuDGTTrSXZywYkmjCC' \
       'EUZShGofaFpuespaZWLFNIsOqsIRLexWqTXsOaScgnsUKsJxiihwsCdBViEQBHQaOnLfB' \
       'tQQShTYHFqrvpVFiiEFMcIFTrTkIBpGUflwTvAzMUtmSlQQZGHmQKJndiAXbIzVkGSeuT' \
       'SkyjIGsiWLALHUCsnQtiOtrbQOQunurZgHFiZjWtZCEXZCnZjLeMiFlxnPkqfJFbCfKCu' \
       'UJmGYJZPpRBFNLkqigxFkrRAppYRXeSCBxbGvqHmlsSZMWSVQyzenWoGxyGPvbnhWHuXB' \
       'qHFjvihuNGEEFsfnMXTfptvIOlhKhyYwxLnqOsBdGvnuyEZIheApQGOXWeXoLWiDQNJFa' \
       'XiUWgsKQrDOeZoNlZNRvHnLgCmysUeKnVJXPFIzvdDyleXylnKBfLCjLHntltignbQoiQ' \
       'zTYwZAiRwycdlHfyHNGmkNqSwXUrxGc'

result = re.findall(r"[a-z]+", line)
print('С использованием re:\n', result)

item = ''
result_without_re = []
for el in line:
    if not el.isupper():
        item += el
    else:
        if item:
            result_without_re.append(item)
            item = ''
print('Без использования re:\n', result_without_re)

# Задание-2:
# Вывести символы в верхнем регистре, слева от которых находятся
# два символа в нижнем регистре, а справа два символа в верхнем регистре.
# Т.е. из строки
# "GAMkgAYEOmHBSQsSUHKvSfbmxULaysmNOGIPHpEMujalpPLNzRWXfwHQqwksrFeipEUlTLec"
# нужно получить список строк: ['AY', 'NOGI', 'P']
# Решить задачу двумя способами: с помощью re и без.

pattern = re.compile(r'[a-z][a-z]([A-Z]+)[A-Z][A-Z]')
result_task_2_with_re = pattern.findall(line)
print('С использованием re:\n', result_task_2_with_re)
j = 0
item = ''
result_task_2_without_re = []
while j < len(line) - 4:
    if not line[j].isupper() and not line[j + 1].isupper() and \
            line[j + 2].isupper():
        j = j + 2
        while line[j].isupper():
            item += line[j]
            j += 1
        j -= 1
        if len(item) >= 3:
            result_task_2_without_re.append(item[:-2])
            item = ''
        else:
            item = ''
            j -= 1
    j += 1
print('Без использования re:\n', result_task_2_without_re)
# Задание-3:
# Напишите скрипт, заполняющий указанный файл (самостоятельно задайте имя
# файла) произвольными целыми цифрами, в результате в файле должно быть
# 2500-значное произвольное число.
# Найдите и выведите самую длинную последовательность одинаковых цифр
# в вышезаполненном файле.
dir_name = os.getcwd()
path = os.path.join(dir_name, 'file_for_number.txt')
pattern_1 = re.compile(r'(0+|1+|2+|3+|4+|5+|6+|7+|8+|9+)')
my_rand_int = ''
while j < 2500:
    my_rand_int += (str(random.randint(0, 9)))
    j += 1
with open(path, 'w', encoding='UTF-8') as f:
    f.write(my_rand_int)
g = open(path, 'r', encoding='UTF-8')
num = g.read()
result_task_3 = pattern_1.findall(num)
set_of_num = set()
for el in result_task_3:
    if len(el) == len(max(result_task_3)):
        set_of_num.add(el)
print(set_of_num)
