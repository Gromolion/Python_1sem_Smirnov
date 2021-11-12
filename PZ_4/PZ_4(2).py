# программа проверяет, является ли заданное значение степенью числа 3
from math import log
n = input('Введите целое число n (n > 0): ')

while type(n) != int or n < 0:
    # обработка исключений

    try:
        n = int(n)

        if n < 0:
            print(n, '< 0')
            n = input('Введите n заново: ')

    except ValueError:
        print('Вы ввели не целое число')
        n = input('Введите n заново: ')

print(f'{n} является степенью числа 3 -', 'TRUE' if log(n, 3) == int(log(n, 3)) else 'FALSE')
# вывод TRUE, если log(n, 3) == int(log(n, 3)), т.к int() убирает дробную часть у чисел, иначе FALSE
