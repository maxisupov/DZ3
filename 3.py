# Задайте список из вещественных чисел. Напишите программу,
# которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
from random import uniform

num = int(input('Введите размер списка: '))
my_list = []
for i in range(num):
    f = uniform(0, 9)
    my_list.append(round(f, 2))

print(my_list)

min_num = my_list[0]
max_num = 0

for i in range(len(my_list)):

    if max_num < my_list[i]:
        max_num = my_list[i]
    if min_num > my_list[i]:
        min_num = my_list[i]

print(max_num, min_num)

print(round(((max_num - int(max_num)) - (min_num - int(min_num))), 2))
