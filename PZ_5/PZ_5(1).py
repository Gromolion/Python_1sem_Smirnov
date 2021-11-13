# программа находит сумму чисел ряда 1, 2, 3, 4, ... от числа n до m
def summa(x, y):
    return sum([i for i in range(x, y + 1)])
    # мы генерируем список с элементами от x до y и используем
    # функцию sum() для получения суммы элементов списка и возвращаем её


n, m = input('Введите числа n и m: ').split()

while type(n) != int or type(m) != int:
    # обработка исключений
    try:
        n = int(n)
        m = int(m)
    except ValueError:
        n, m = input('Одно из значений не является числом. Введите числа n и m заново: ').split()

print('Сумма чисел от n до m:', summa(n, m))
