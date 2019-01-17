# Задание-1: уравнение прямой вида y = kx + b задано в виде строки.
# Определить координату y точки с заданной координатой x.

# equation = 'y = -12x + 11111140.2121'
# x = 2.5
# вычислите и выведите y

print("\nЗадача №1")

formula = ("y = -12x + 11111140.2121")
x = float(2.5)
s1 = int(formula.rfind("+"))
s2 = int(formula.rfind("="))
s3 = int(formula.rfind("x"))
b = formula[(s1+1):]
b_num = float(b)
k = formula[(s2+1):s3]
k_num = float(k)
y = x * k_num + b_num
print("\n формула: {} \n x = {} \n y = {}".format(formula, x, y))




# Задание-2: Дата задана в виде строки формата 'dd.mm.yyyy'.
# Проверить, корректно ли введена дата.
# Условия корректности:
# 1. День должен приводиться к целому числу в диапазоне от 1 до 30(31)
#  (в зависимости от месяца, февраль не учитываем)
# 2. Месяц должен приводиться к целому числу в диапазоне от 1 до 12
# 3. Год должен приводиться к целому положительному числу в диапазоне от 1 до 9999
# 4. Длина исходной строки для частей должна быть в соответствии с форматом
#  (т.е. 2 символа для дня, 2 - для месяца, 4 - для года)

# Пример корректной даты
date = '01.11.1985'

# Примеры некорректных дат
date = '01.22.1001'
date = '1.12.1001'
date = '-2.10.3001'

print("\nЗадача №2")

data_input = input("Введите дату в формате dd.mm.yyyy:")
raw_data = data_input.split(".")
print(raw_data)
if len(raw_data) != 3:
    print("не полные данные")
else:
    if (len(raw_data[0]) != 2) or (len(raw_data[1]) != 2) or (len(raw_data[2]) != 4):
        print("не верный формат данных")
    else:
        date = int(raw_data[0])
        month = int(raw_data[1])
        year = int(raw_data[2])
        if 0 < year < 10000:
            if 0 < month < 13:
                if 0 < date < 31:
                    print("формат данный верен")
                else:
                    print("ошибка ввода даты")
            else:
                print("ошибка ввода месяца")
        else:
            print("ошибка ввода года")


# Задание-3: "Перевёрнутая башня" (Задача олимпиадного уровня)
#
# Вавилонцы решили построить удивительную башню —
# расширяющуюся к верху и содержащую бесконечное число этажей и комнат.
# Она устроена следующим образом — на первом этаже одна комната,
# затем идет два этажа, на каждом из которых по две комнаты,
# затем идёт три этажа, на каждом из которых по три комнаты и так далее:
#         ...
#     12  13  14
#     9   10  11
#     6   7   8
#       4   5
#       2   3
#         1
#
# Эту башню решили оборудовать лифтом --- и вот задача:
# нужно научиться по номеру комнаты определять,
# на каком этаже она находится и какая она по счету слева на этом этаже.
#
# Входные данные: В первой строчке задан номер комнаты N, 1 ≤ N ≤ 2 000 000 000.
#
# Выходные данные:  Два целых числа — номер этажа и порядковый номер слева на этаже.
#
# Пример:
# Вход: 13
# Выход: 6 2
#
# Вход: 11
# Выход: 5 3
