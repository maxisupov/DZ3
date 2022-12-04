# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов (Негафибоначчи).

my_list = [0]
number = int(input('Введите число: '))


def Fibonacci(n):
    if n in [1, 2]:
        return 1
    else:
        return Fibonacci(n - 1) + Fibonacci(n - 2)


def NegaFibonacci(n):
    if n == 1:
        return 1
    elif n == 2:
        return -1
    else:
        num1 = 1
        num2 = -1
        for i in range(2, n):
            num1, num2 = num2, num1 - num2
        return num2


for i in range(1, number + 1):
    my_list.append(Fibonacci(i))
    my_list.insert(0, NegaFibonacci(i))

print(my_list)
