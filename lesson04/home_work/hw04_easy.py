# Все задачи текущего блока решите с помощью генераторов списков!

# Задание-1:
# Дан список, заполненный произвольными целыми числами.
# Получить новый список, элементы которого будут
# квадратами элементов исходного списка
# [1, 2, 4, 0] --> [1, 4, 16, 0]

print("\n\nЗадание №1\n")

import random
lst = [random.randint(0, 10) for _ in range(10)]
print(lst)
lst_sq = [_ ** 2 for _ in lst]
print(lst_sq)

# Задание-2:
# Даны два списка фруктов.
# Получить список фруктов, присутствующих в обоих исходных списках.



print("\n\nЗадание №2\n")

import random

fruits = ["apple", "banana", "pear", "watermelon", "apricot", "pineapple", "grape", "melone", "grapefruit", "lemon",
          "tangerine", "peach", "plum", "kiwi", "fig", "mango"]

lq1 = random.randint(1, 10)
lq2 = random.randint(1, 10)

list1 = [random.choices(fruits) for _ in range(lq1)]
list2 = [random.choices(fruits) for _ in range(lq2)]
list3 = [x for x in list1 if x in list2]

print(list1)
print(list2)
print(list3)


print("\n\nЗадание №2 (доп решение)\n")
"""
    
    вариант со списками без повторов
    
    """
import random

fruits = ["apple", "banana", "pear", "watermelon", "apricot", "pineapple", "grape", "melone", "grapefruit", "lemon",
          "tangerine", "peach", "plum", "kiwi", "fig", "mango"]

lq1 = random.randint(1, 10)
lq2 = random.randint(1, 10)

list1 = random.sample(set(fruits), int(lq1))
list2 = random.sample(set(fruits), int(lq2))
list3 = [x for x in list1 if x in list2]

print(list1)
print(list2)
print(list3)



# Задание-3:
# Дан список, заполненный произвольными числами.
# Получить список из элементов исходного, удовлетворяющих следующим условиям:
# + Элемент кратен 3
# + Элемент положительный
# + Элемент не кратен 4


print("\n\nЗадание №3\n")
import random

n = random.randint(1, 100)
numbers = [random.randint(-100, 100) for _ in range(n)]
list_cond = [x for x in numbers if x % 3 == 0 and x % 4 != 0 and x > 0]

print(numbers, "\n", list_cond)
