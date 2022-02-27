# В матрице найти сумму элементов второй половины матрицы
# я решал задачу, считая, что вторая половина начинается с серединного элемента серединной строки матрицы

from random import randint

columns = randint(3, 10)  # задаю рандомное число столбцов матрицы
rows = randint(3, 10)  # рандомное число строк
summa = 0
matrix = [[randint(-5, 5) for i in range(columns)] for j in range(rows)]  # создаю матрицу

for i in range(int(rows / 2), rows):  # внешним циклом прохожусь по матрице, начиная с серединной строки,

    if i == int(rows / 2):  # первая нужная строка складывается вне внутреннего цикла

        if rows % 2 == 0:  # проверка на четность количества строк
            summa += sum(matrix[i])  # если четно - складывается вся первая нужная строка
        else:
            summa += sum(matrix[i][int(columns / 2):])  # иначе - половина строки
        continue

    for j in range(columns):
        summa += matrix[i][j]  # во внутреннем цикле складываем оставшиеся строки

print('Матрица:')

for i in matrix:
    print(i)

print(f'Сумма: {summa}')
