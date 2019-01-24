# Задание-1:
# Вывести символы в нижнем регистре, которые находятся вокруг
# 1 или более символов в верхнем регистре.
# Т.е. из строки "mtMmEZUOmcq" нужно получить ['mt', 'm', 'mcq']
# Решить задачу двумя способами: с помощью re и без.

print("\n\nЗадание №1\n")

import re

line = 'mtMmEZUOmcqWiryMQhhTxqKdSTKCYEJlEZCsGAMkgAYEOmHBSQsSUHKvSfbmxULaysmNO'\
    'GIPHpEMujalpPLNzRWXfwHQqwksrFeipEUlTLeclMwAoktKlfUBJHPsnawvjPhfgewVzK'\
        'TUfSYtBydXaVIpxWjNKgXANvIoumesCSSvjEGRJosUfuhRRDUuTQwLlJJJDdkVjfSAHqn'\
            'LxooisBDWuxIhyjJaXDYwdoVPnsllMngNlmkpYOlqXEFIxPqqqgAWdJsOvqppOfyIVjXa'\
                'pzGOrfinzzsNMtBIOclwbfRzytmDgEFUzxvZGkdOaQYLVBfsGSAfJMchgBWAsGnBnWete'\
                    'kUTVuPluKRMQsdelzBgLzuwiimqkFKpyQRzOUyHkXRkdyIEBvTjdByCfkVIAQaAbfCvzQ'\
                        'WrMMsYpLtdqRltXPqcSMXJIvlBzKoQnSwPFkapxGqnZCVFfKRLUIGBLOwhchWCdJbRuXb'\
                            'JrwTRNyAxDctszKjSnndaFkcBZmJZWjUeYMdevHhBJMBSShDqbjAuDGTTrSXZywYkmjCC'\
                                'EUZShGofaFpuespaZWLFNIsOqsIRLexWqTXsOaScgnsUKsJxiihwsCdBViEQBHQaOnLfB'\
                                    'tQQShTYHFqrvpVFiiEFMcIFTrTkIBpGUflwTvAzMUtmSQQZGHlmQKJndiAXbIzVkGSeuT'\
                                        'SkyjIGsiWLALHUCsnQtiOtrbQOQunurZgHFiZjWtZCEXZCnZjLeMiFlxnPkqfJFbCfKCu'\
                                            'UJmGYJZPpRBFNLkqigxFkrRAppYRXeSCBxbGvqHmlsSZMWSVQyzenWoGxyGPvbnhWHuXB'\
                                                'qHFjvihuNGEEFsfnMXTfptvIOlhKhyYwxLnqOsBdGvnuyEZIheApQGOXWeXoLWiDQNJFa'\
                                                    'XiUWgsKQrDOeZoNlZNRvHnLgCmysUeKnVJXPFIzvdDyleXylnKBfLCjLHntltignbQoiQ'\
                                                        'zTYwZAiRwycdlHfyHNGmkNqSwXUrxGc'

found = re.findall(r'[a-z]+', line)
l = len(found)
i = 0
while i < l:
    print(found[i:i+15])
    i += 15

# Задание-2:
# Вывести символы в верхнем регистре, слева от которых находятся
# два символа в нижнем регистре, а справа - два символа в верхнем регистре.
# Т.е. из строки
# "GAMkgAYEOmHBSQsSUHKvSfbmxULaysmNOGIPHpEMujalpPLNzRWXfwHQqwksrFeipEUlTLec"
# нужно получить список строк: ['AY', 'NOGI', 'P']
# Решить задачу двумя способами: с помощью re и без.

print("\n\nЗадание №2\n")

import re

line_2 = 'mtMmEZUOmcqWiryMQhhTxqKdSTKCYEJlEZCsGAMkgAYEOmHBSQsSUHKvSfbmxULaysm'\
    'NOGIPHpEMujalpPLNzRWXfwHQqwksrFeipEUlTLeclMwAoktKlfUBJHPsnawvjPhfgewV'\
        'fzKTUfSYtBydXaVIpxWjNKgXANvIoumesCSSvjEGRJosUfuhRRDUuTQwLlJJJDdkVjfSA'\
            'HqnLxooisBDWuxIhyjJaXDYwdoVPnsllMngNlmkpYOlqXEFIxPqqqgAWdJsOvqppOfyIV'\
                'jXapzGOrfinzzsNMtBIOclwbfRzytmDgEFUzxvZGkdOaQYLVBfsGSAfJMchgBWAsGnBnW'\
                    'etekUTVuPluKRMQsdelzBgLzuwiimqkFKpyQRzOUyHkXRkdyIEBvTjdByCfkVIAQaAbfC'\
                        'vzQWrMMsYpLtdqRltXPqcSMXJIvlBzKoQnSwPFkapxGqnZCVFfKRLUIGBLOwhchWCdJbR'\
                            'uXbJrwTRNyAxDctszKjSnndaFkcBZmJZWjUeYMdevHhBJMBSShDqbjAuDGTTrSXZywYkm'\
                                'jCCEUZShGofaFpuespaZWLFNIsOqsIRLexWqTXsOaScgnsUKsJxiihwsCdBViEQBHQaOn'\
                                    'LfBtQQShTYHFqrvpVFiiEFMcIFTrTkIBpGUflwTvAzMUtmSQQZGHlmQKJndiAXbIzVkGS'\
                                        'euTSkyjIGsiWLALHUCsnQtiOtrbQOQunurZgHFiZjWtZCEXZCnZjLeMiFlxnPkqfJFbCf'\
                                            'KCuUJmGYJZPpRBFNLkqigxFkrRAppYRXeSCBxbGvqHmlsSZMWSVQyzenWoGxyGPvbnhWH'\
                                                'uXBqHFjvihuNGEEFsfnMXTfptvIOlhKhyYwxLnqOsBdGvnuyEZIheApQGOXWeXoLWiDQN'\
                                                    'JFaXiUWgsKQrDOeZoNlZNRvHnLgCmysUeKnVJXPFIzvdDyleXylnKBfLCjLHntltignbQ'\
                                                        'oiQzTYwZAiRwycdlHfyHNGmkNqSwXUrxGC'

found = re.findall(r"[a-z]{2}([A-Z]+)[A-Z]{2}", line_2)
l = len(found)
i = 0
while i < l:
    print(found[i:i+15])
    i += 15


print("\n\nЗадание №2 (без re)\n")

line_2 = 'mtMmEZUOmcqWiryMQhhTxqKdSTKCYEJlEZCsGAMkgAYEOmHBSQsSUHKvSfbmxULaysm' \
    'NOGIPHpEMujalpPLNzRWXfwHQqwksrFeipEUlTLeclMwAoktKlfUBJHPsnawvjPhfgewV' \
        'fzKTUfSYtBydXaVIpxWjNKgXANvIoumesCSSvjEGRJosUfuhRRDUuTQwLlJJJDdkVjfSA' \
            'HqnLxooisBDWuxIhyjJaXDYwdoVPnsllMngNlmkpYOlqXEFIxPqqqgAWdJsOvqppOfyIV' \
                'jXapzGOrfinzzsNMtBIOclwbfRzytmDgEFUzxvZGkdOaQYLVBfsGSAfJMchgBWAsGnBnW' \
                    'etekUTVuPluKRMQsdelzBgLzuwiimqkFKpyQRzOUyHkXRkdyIEBvTjdByCfkVIAQaAbfC' \
                        'vzQWrMMsYpLtdqRltXPqcSMXJIvlBzKoQnSwPFkapxGqnZCVFfKRLUIGBLOwhchWCdJbR' \
                            'uXbJrwTRNyAxDctszKjSnndaFkcBZmJZWjUeYMdevHhBJMBSShDqbjAuDGTTrSXZywYkm' \
                                'jCCEUZShGofaFpuespaZWLFNIsOqsIRLexWqTXsOaScgnsUKsJxiihwsCdBViEQBHQaOn' \
                                    'LfBtQQShTYHFqrvpVFiiEFMcIFTrTkIBpGUflwTvAzMUtmSQQZGHlmQKJndiAXbIzVkGS' \
                                        'euTSkyjIGsiWLALHUCsnQtiOtrbQOQunurZgHFiZjWtZCEXZCnZjLeMiFlxnPkqfJFbCf' \
                                            'KCuUJmGYJZPpRBFNLkqigxFkrRAppYRXeSCBxbGvqHmlsSZMWSVQyzenWoGxyGPvbnhWH' \
                                                'uXBqHFjvihuNGEEFsfnMXTfptvIOlhKhyYwxLnqOsBdGvnuyEZIheApQGOXWeXoLWiDQN' \
                                                    'JFaXiUWgsKQrDOeZoNlZNRvHnLgCmysUeKnVJXPFIzvdDyleXylnKBfLCjLHntltignbQ' \
                                                        'oiQzTYwZAiRwycdlHfyHNGmkNqSwXUrxGC'

Up_S = list(map(lambda x: chr(x), list(range(65, 91))))  # Преобразуем список из кодов ANSI в список букв A-Z
S_S = list(map(lambda x: chr(x), list(range(97, 123))))  # Преобразуем список из кодов ANSI в список букв a-z
line_3 = list(line_2)

lst_dr = []
i = len(line_3) - 1

while i >= 0:
    if line_3[i] in S_S:
        lst_dr.append(line_3[i])
    elif line_3[i] in Up_S and i <= len(line_3) - 3 and line_3[i + 1] in Up_S and line_3[i + 2] in Up_S:
        lst_dr.append(line_3[i])
    else:
        lst_dr.append(' ')
    i -= 1
lst_dr.reverse()  # Переворачиваем список

i = 0
lst2 = []
chek = True

while i <= len(lst_dr) - 1:
    if lst_dr[i] in S_S:
        chek = True
    if lst_dr[i] in Up_S and lst_dr[i - 1] in S_S and lst_dr[i - 2] in S_S:
        lst2.append(lst_dr[i])
        chek = False
    elif lst_dr[i] in Up_S and chek == False:
        lst2.append(lst_dr[i])
    else:
        lst2.append(' ')
    i += 1
line_it = ''.join(lst2).split(' ')

line_it_str = [i for i in line_it if i != '']
l = len(line_it_str)
i = 0
while i < l:
    print(line_it_str[i:i + 15])
    i += 15

# Задание-3:
# Напишите скрипт, заполняющий указанный файл (самостоятельно задайте имя файла)
# произвольными целыми цифрами, в результате в файле должно быть
# 2500-значное произвольное число.
# Найдите и выведите самую длинную последовательность одинаковых цифр
# в вышезаполненном файле.


import random
import re


number = [random.randint(0, 9) for _ in range(2500)]
# number = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 1, 1]
number_str = (list(map(lambda x: str(x), number)))
line =''.join(number_str)
print(number)
print(line)

path = 'data\\' + 'script_hw04_3' + '.txt'
with open(path, 'w', encoding='UTF-8') as file:
    file.write(str(line))

f0 = max(re.findall(r"[0]*", line))
f1 = max(re.findall(r"[1]*", line))
f2 = max(re.findall(r"[2]*", line))
f3 = max(re.findall(r"[3]*", line))
f4 = max(re.findall(r"[4]*", line))
f5 = max(re.findall(r"[5]*", line))
f6 = max(re.findall(r"[6]*", line))
f7 = max(re.findall(r"[7]*", line))
f8 = max(re.findall(r"[8]*", line))
f9 = max(re.findall(r"[9]*", line))


aa = [f0,f1,f2,f3,f4,f5,f6,f7,f8,f9]
print(aa)
max_len = len(aa[0])
a = []
a = aa[0]

for i in range(10):
    if len(aa[i]) >= max_len:
        max_len = len(aa[i])
        a = aa[i]
print(" Максимальная последовательность {} - {} повторений подряд".format(a, max_len))


