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
    7 11     - 14    87
    16 49    55 77    88
    15 20     -       76  -
    --------------------------
    Зачеркнуть цифру? (y/n)
    
    Подсказка: каждый следующий случайный бочонок из мешка удобно получать
    с помощью функции-генератора.
    
    Подсказка: для работы с псевдослучайными числами удобно использовать
    модуль random: http://docs.python.org/3/library/random.html
    
    """

import random

class Card:
    def __init__(self, name):
        bag = [x for x in range(1, 91)]  # все бочонки
        self.card = [__class__.gen_string(bag), __class__.gen_string(bag),
                     __class__.gen_string(bag)]
                     self.name = name
                     self.count_barrel = 15  # цифр на карточке, осталось

@staticmethod
    def gen_string(bag):
        string = ['' for _ in range(9)]
        for x in range(8, 3, -1):
            digit = random.randint(0, x)  # место в строке на карточке, которое заполняется
            while string[digit] != '':  # если место в строке уже заполнено
                digit += 1
            string[digit] = bag.pop(random.randint(0, len(bag) - 1))
        return string
    
    def __str__(self):
        rez = '{:=^27}\n'.format(self.name)
        for x in range(3):
            rez += '{:>2} {:>2} {:>2} {:>2} {:>2} {:>2} {:>2} {:>2} {:>2}'\
                .format(*self.card[x]) + '\n'
        return rez + '=' * 27


player = Card(" Карточка игрока ")
computer = Card(" Карточка компьютера ")
bag = [x for x in range(1, 91)]  # Мешок с бочками.
while True:
    if len(bag) < 1:
        print("Бочёнки в мешке закончились. Результат:\n"
              "у Компьютера осталось {} мест,\n"
              "у игрока осталось {} мест."
              .format(computer.count_barrel, player.count_barrel))
        break
    barrel = bag.pop(random.randint(0, len(bag) - 1))
    print("\nНовый бочонок: {} (осталось {})".format(barrel, len(bag)))
    print(player)
    print(computer)
    reply = input("Зачеркнуть цифру? (y/n/q)")
    reply = reply.lower()
    while len(reply) == 0 or reply not in "ynq":
        print("\n\nНе корректный выбор\n")
        print("Новый бочонок: {} (осталось {})".format(barrel, len(bag)))
        print(computer)
        print(player)
        reply = input("Зачеркнуть цифру? (y/n/q)")
        reply = reply.lower()
    
    if reply == 'q':
        print("Игра прервана")
        break
    elif reply == "y":
        test = False  # Проверка наличия цифры на карте игрока
        for x in range(3):
            if barrel in player.card[x]:
                test = True
                player.card[x][player.card[x].index(barrel)] = "-"
                player.count_barrel -= 1
            if barrel in computer.card[x]:
                computer.card[x][computer.card[x].index(barrel)] = "-"
                computer.count_barrel -= 1
        if test:
            if player.count_barrel < 1:
                print("Вы Выиграли!")
                break
            elif computer.count_barrel < 1:
                print("Компьютер Выиграл!")
                break
        else:
            print("Вы проиграли! Такого числа нет на вашей карточке!")
            break
    elif reply == "n":
        test = False  # Есть ли такая цифра на карточке игрока?
        for x in range(3):
            if barrel in player.card[x]:
                print("Вы проиграли! Такое число есть на Вашей карточке!")
                test = True
                break
            if barrel in computer.card[x]:
                computer.card[x][computer.card[x].index(barrel)] = "-"
                computer.count_barrel -= 1
        if test:
            break
        if player.count_barrel < 1:
            print("Вы выиграли!")
            break
        elif computer.count_barrel < 1:
            print("Компьютер выиграл!")
            break

