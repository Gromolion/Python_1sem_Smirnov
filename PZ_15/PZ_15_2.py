# В матрице элементы второго столбца возвести в квадрат

from random import randint

rows = randint(3, 6)
columns = randint(3, 6)
matrix = [[randint(-5, 5) for i in range(columns)] for j in range(rows)]

print('Матрица:')
for i in matrix:
    print(i)

for j in range(rows):
    matrix[j][1] = matrix[j][1] ** 2

print('\nНовая матрица:')
for i in matrix:
    print(i)
