# программе дается два списка длиной N.
# Сформировать новый список С того же размера, каждый элемент которого равен
# максимальному из элементов списков A и B
import random

n = int(input('Введите длину списков: '))
a = [random.randint(1, 100) for i in range(n)]
b = [random.randint(1, 100) for i in range(n)]
c = [max(a[i], b[i]) for i in range(n)]
print(c)
