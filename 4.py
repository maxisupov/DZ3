# Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# Без применения встроенных методов (арифметически)

num = int(input('Введите число:  '))


def binCode(num):
    if (num == 0):
        return '0'
    binNum = ''
    while (num > 0):
        if (num & 1 == 0):
            binNum = '0' + binNum
        else:
            binNum = '1' + binNum
        num = num >> 1
    return binNum


print(binCode(num))
