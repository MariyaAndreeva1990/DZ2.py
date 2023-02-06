"""
Задача 14: Требуется вывести все целые степени двойки 
(т.е. числа вида 2k), не превосходящие числа N.
10 -> 1 2 4 8
"""
n = int(input('Введите число: '))
degree = 0
number = 2
while number <= n:
        number = 2**degree
        degree +=1
        if number <= n:
                print (number, end = ' ')
        else:
                print ()
