# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка с нечетными индексами.

my_list = [2, 23, 12, 10, 12, 16, 5]
summ = 0

print(my_list)
for i in range(len(my_list)):
    if i % 2 == 1:
        summ += my_list[i]
print(f"Cумма элементов на нечётных позициях: {summ}")
