# программа должна проверять, чередуются ли в списке размера N четные и нечетные числа.
# Если чередуются, то вывести 0, если нет, то вывести порядковый номер первого элемента,
# нарушающего закономерность
import random

n = int(input('Введите длину списка: '))
mylist = [random.randint(1, 2) for el in range(n)]
result = 0
# выводим список для наглядности
for i in range(1, len(mylist)):
    if mylist[i - 1] % 2 == mylist[i] % 2:
        result = i
        break
print(result)
