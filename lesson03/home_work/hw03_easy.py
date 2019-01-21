# Задание-1:
# Напишите функцию, округляющую полученное произвольное десятичное число
# до кол-ва знаков (кол-во знаков передается вторым аргументом).
# Округление должно происходить по математическим правилам (0.6 --> 1, 0.4 --> 0).
# Для решения задачи не используйте встроенные функции и функции из модуля math.

def my_round(number, ndigits):
    r = number * (10 ** ndigits)
    o = r % 1
    if o > 0.5:
        round_number = (r - o + 1)/(10 ** ndigits)
    else:
        round_number = (r - o)/(10 ** ndigits)
    return round_number

print(my_round(2.1234567, 5))
print(my_round(2.1999967, 5))
print(my_round(2.9999967, 5))


# Задание-2:
# Дан шестизначный номер билета. Определить, является ли билет счастливым.
# Решение реализовать в виде функции.
# Билет считается счастливым, если сумма его первых и последних цифр равны.
# !!!P.S.: функция не должна НИЧЕГО print'ить

def lucky_ticket(ticket_number):
    tn = str(ticket_number)
    lt = list(map(lambda x: int(x), tn))
    lt1 = lt[:3]
    lt2 = lt[3:]
    sum1 = 0
    for i in lt1:
        sum1 = sum1 + i
    
    sum2 = 0
    for i in lt2:
        sum2 = sum2 + i

    luck = sum1 - sum2

if luck == 0:
    return luck == 0


print(lucky_ticket(123006))
print(lucky_ticket(12321))
print(lucky_ticket(436751))
