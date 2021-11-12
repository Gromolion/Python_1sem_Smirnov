import random

n1 = int(input('Введите n1: '))
n2 = int(input('Введите n2: '))
a = {(random.randint(-100, 100), random.randint(-100, 100)) for i in range(n1)}
b = {(random.randint(-100, 100), random.randint(-100, 100)) for j in range(n2)}
minR = 999999
minR_point1 = tuple()
minR_point2 = tuple()
for point1 in a:
    for point2 in b:
        if ((point2[0] - point1[0])**2 + (point2[1] - point1[1])**2)**(1/2) < minR:
            minR = ((point2[0] - point1[0])**2 + (point2[1] - point1[1])**2)**(1/2)
            minR_point1 = point1
            minR_point2 = point2
print(f'Минимальное расстояние между точками = {minR}')
print(f'Точки:\n'
      f'Из множества А: {minR_point1},\n'
      f'Из множества В: {minR_point2}')
