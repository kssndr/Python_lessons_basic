# Задание-1:
# Напишите функцию, возвращающую ряд Фибоначчи с n-элемента до m-элемента.
# Первыми элементами ряда считать цифры 1 1


"""
    построения ряда с помощью формулы Бине
    
    """

def fibonacci(n, m):
    n_ = n
    m_ = m + 1
    rf = []
    gs = (1 + 5 ** 0.5) / 2
    for i in range(0, m_):
        f = int((gs ** i - (- gs ** (-i))) / (2 * gs - 1))
        rf.append(f)
    rf = rf[n_:m_]
    return rf
n = int(input("Задайте диапозон для вывода ряда Фибоначчи\n n: "))
m = int(input(" m: "))
print(fibonacci(n, m))

"""
    построения ряда с помощью кортежа
    
    """

def fib(n, m):
    first = 0
    second = 1
    rf2 = []
    for i in range(m):
        rf2.append(second)
        first, second = second, second + first
    n -= 1
    fib_nm = [rf2[a] for a in range(n,m)]
    return fib_nm


n = int(input("Задайте диапозон для вывода ряда Фибоначчи\n n: "))
m = int(input(" m: "))
print(fib(10, 14))




# Задача-2:
# Напишите функцию, сортирующую принимаемый список по возрастанию.
# Для сортировки используйте4 любой алгоритм (например пузырьковый).
# Для решения данной задачи нельзя использовать встроенную функцию и метод sort()


def sort_to_max(origin_list):
    numbers = list(origin_list)
    l_n = len(numbers)
    n = 1
    while n < l_n:
        for i in range(l_n - n):
            if numbers[i] > numbers[i + 1]:
                numbers[i], numbers[i + 1] = numbers[i + 1], numbers[i]
        n += 1
    
    return print(numbers)

sort_to_max([2, 10, -12, 2.5, 20, -11, 4, 4, 0])

# Задача-3:
# Напишите собственную реализацию стандартной функции filter.
# Разумеется, внутри нельзя использовать саму функцию filter.


l = "j4mnw4;efvf52jsdcsd5320sEDs124dv69"
"""
    фильтр для выявления цифр в строке
    
    """


def find_numbers(list_):
    numbers = []
    for i in list_:
        if '0' <= i <= '9':
            numbers.append(i)
    return numbers


print(find_numbers(l))


# Задача-4:
# Даны четыре точки А1(х1, у1), А2(x2 ,у2), А3(x3 , у3), А4(х4, у4).
# Определить, будут ли они вершинами параллелограмма.

'''
    Четырёхугольник ABCD является параллелограммом, если выполняется одно из следующих условий (в этом случае выполняются и все остальные):
    У четырёхугольника без самопересечений две противоположные стороны одновременно равны и параллельны:
    
    У четырёхугольника без самопересечений все противоположные стороны попарно равны: AB = CD, AD = BC
    
    '''


def def_paral(A, B, C, D):
    x1, y1 = A
    x2, y2 = B
    x3, y3 = C
    x4, y4 = D
    AB = ((x1 - x2) ** 2 - (y1 - y2) ** 2) ** 0.5
    CD = ((x3 - x4) ** 2 - (y3 - y4) ** 2) ** 0.5
    AD = ((x1 - x4) ** 2 - (y1 - y4) ** 2) ** 0.5
    BC = ((x2 - x3) ** 2 - (y2 - y3) ** 2) ** 0.5
    
    print(x1, x2, x3, x4, y1, y2, y3, y4)
    print(AB, CD, AD, BC)
    if AB == CD and AD == BC:
        return print("Это параллелограмм")
    else:
        return print("Это не параллелограмм")

def_paral((10, 20), (10, 40), (20, 40), (20, 20))
