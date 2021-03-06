# Задача-1:
# Напишите небольшую консольную утилиту,
# позволяющую работать с папками текущей директории.
# Утилита должна иметь меню выбора действия, в котором будут пункты:
# 1. Перейти в папку
# 2. Просмотреть содержимое текущей папки
# 3. Удалить папку
# 4. Создать папку
# При выборе пунктов 1, 3, 4 программа запрашивает название папки
# и выводит результат действия: "Успешно создано/удалено/перешел",
# "Невозможно создать/удалить/перейти"

# Для решения данной задачи используйте алгоритмы из задания легко,
# оформленные в виде соответствующих функций,
# и импортированные в данный файл из easy.py
import os
import easy

#9
exitos = 'a'
while exitos != '0':
    print("__________________")
    print("Перейти в папку - 1")
    print("Просмотреть содержимое текущей папки - 2")
    print("Удалить папку - 3")
    print("Создать папку - 4")
    print("Выход - 0")
    exitos = input("Выбрать: ")
    print("_______")
    print("Ваш выбор:", exitos)
    if exitos == "1":
        print("Запрашиваемый результат:")
        dir_name = input("Введите полный путь папки: ")
        easy.change_dir(dir_name)
    elif exitos == "2":
        dir_name = os.getcwd()
        easy.list_dir(dir_name)
    elif exitos == "3":
        dir_name = input("Введите полный путь папки: ")
        easy.delete_dir(dir_name)
    elif exitos == "4":
        dir_name = input("ВВедите полный путь папки: ")
        easy.make_dir(dir_name)
    elif exitos == "0":
        pass
    else:
        print("Такого пункта меню нет")