﻿# Python_B1_1_DmitrievaOA_1432_05

print("Enter a number:") # Введите число: - выводим текст на экран
num1 = float(input()) # запрашиваем у пользователя ввод числа (и сохраняем его, приводя к типу float)
print("Enter a boundary number:") # Введите номер границы:
boundary = float(input()) # запрашиваем у пользователя ввод пограничного числа (и сохраняем его, приводя к типу float)

if num1 < boundary: # если 1-ое число меньше пограничного
    print("The first number is less than the boundary.") # Первое число меньше границы.
elif num1 > boundary: # если 1-ое число больше пограничного
    print("The first number is greater than the boundary.") # Первое число больше границы.
    if num1 > boundary * 3: # если 1-ое число больше пограничного более, чем в 3 раза
        print("The first number is more than 3 times greater than the boundary.") # Первое число больше границы более чем в 3 раза.
