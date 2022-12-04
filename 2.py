# Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.

from random import randint


number = int(input('Введите размер списка:  '))
rnd_list = []
multi_list = []

for i in range(number):
    rnd_list.append(randint(0, 9))

print(rnd_list)

for i in range(len(rnd_list)):
    while i < len(rnd_list)/2 and number > len(rnd_list)/2:
        number = number - 1
        a = rnd_list[i] * rnd_list[number]
        multi_list.append(a)
        i += 1

print(multi_list)