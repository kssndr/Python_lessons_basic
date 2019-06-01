
__author__ = 'Химченко Александр Константинович'

# Задача-1: Дано произвольное целое число, вывести самую большую цифру этого числа.
# Например, дается x = 58375.
# Нужно вывести максимальную цифру в данном числе, т.е. 8.
# Подразумевается, что мы не знаем это число заранее.
# Число приходит в виде целого беззнакового.
# Подсказки:
# * постарайтесь решить задачу с применением арифметики и цикла while;
# * при желании и понимании решите задачу с применением цикла for.

n = str(input("Input number: "))
l = len(n)
biggest = 0
i = 0
while i < l:
    a = n[i]
    if biggest <= int(a):
        biggest = int(a)
    else:
        biggest = biggest
    i = i + 1
print("biggest: ", biggest)
#_________for
n = str(input("Input number: "))
l = len(n)
biggest = 0
for i in range(l):
    a = n[i]
    if biggest <= int(a):
        biggest = int(a)
    else:
        biggest = biggest
print("biggest: ", biggest)

# Задача-2: Исходные значения двух переменных запросить у пользователя.
# Поменять значения переменных местами. Вывести новые значения на экран.
# Решите задачу, используя только две переменные.
# Подсказки:
# * постарайтесь сделать решение через действия над числами;
# * при желании и понимании воспользуйтесь синтаксисом кортежей Python.
# Арифметически

n1 = int(input('Please, input 1st number: '))
n2 = int(input('Please, input 2nd number: '))
n1 = n1 + n2
n2 = n1 - n2
n1 = n1 - n2
print("Now 1st number is:", n1)
print("Now 2nd number is:", n2)

# Кортеж
n1 = int(input('Please, input 1st number: '))
n2 = int(input('Please, input 2nd number: '))
n1, n2 = n2, n1
print("Now 1st number is:", n1)
print("Now 2nd number is:", n2)

# Задача-3: Напишите программу, вычисляющую корни квадратного уравнения вида
# ax² + bx + c = 0.
# Коэффициенты уравнения вводятся пользователем.
# Для вычисления квадратного корня воспользуйтесь функцией sqrt() модуля math:
# import math
# math.sqrt(4) - вычисляет корень числа 4

import math
print("ax^2 + bx + c = 0")
a = int(input('Please, input a: '))
b = int(input('Please, input b: '))
c = int(input('Please, input c: '))
d = b ^ 2 - 4*a*c
print(d)
if d > 0:
    x1 = (-b + math.sqrt(d))/(2 * a)
    x2 = (-b - math.sqrt(d))/(2 * a)
    print(x1, x2)
elif d == 0:
    x1 = - (b / (2 * a))
    x2 = x1
    print(x1, x2)
elif d < 0:
    print("no x1, x2")
    