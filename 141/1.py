def mysum(arr):
    if len(arr) == 1:
        return arr[0]
    return arr[0] + mysum(arr[1:])

def negative_count(arr):
    if len(arr) == 1:
        if arr[0] < 0:
            return 1
        return 0
    return (1 if arr[0]< 0 else 0) + negative_count(arr[1:])


def mysum_with_includes(arr):
    if len(arr) == 1:
        return arr[0]
    if type(arr[0]) == list:
        return mysum_with_includes(arr[0]) + mysum_with_includes(arr[1:])
    return arr[0] + mysum_with_includes(arr[1:])


def fib(n, buff=[1, 1]):
    num1 = buff[-1]
    num2 = buff[-2]

    if (num1 + num2) < n:
        buff += [num1 + num2]
        return fib(n, buff)
    else:
        return buff


def reversing(number):
    number = str(number)
    if len(number) == 1:
        return number
    return number[-1] + reversing(number[:-1])


def power(x, y):
    if y == 0:
        return 1
    return x * power(x, y - 1)


def max_el(arr):
    if len(arr) == 1:
        return arr[0]
    return arr[0] if arr[0] > max_el(arr[1:]) else max_el(arr[1:])


def from_10_to_2(number, k=0):
    if number > 0:
        return from_10_to_2(number // 2, k+1) + int(number % 2 * power(10, k))
    else:
        return 0

print('\nВычисление суммы элементов набора чисел ([1, 2, 3, 4]):')
print(mysum([1, 2, 3, 4]))
print('Вычисление количество отрицательных чисел в наборе([1, -1, -2, -1]):')
print(negative_count([1, -1, -2, -1]))
print('Вычисление суммы чисел с поддержкой вложенных списков([1, 2, [1, 2, 2], 3, 4]):')
print(mysum_with_includes([1, 2, [1, 2, 2], 3, 4]))
print('Возврат ряда Фиббоначи(4):')
print(fib(4))
print('Реверсирование числа(1232):')
print(reversing(1232))
print('Возведение числа x в степень y(3, 10):')
print(power(3, 10))
print('Определение максимального элемента списка([1, 7, 4, 2]):')
print(max_el([1, 7, 4, 2]))
print('Перевод из 10-ой системы исчисления в 2-ю(15):')
print(from_10_to_2(15))
