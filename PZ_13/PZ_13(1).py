# Дана последовательность целых чисел. Поменять местами первую и последнюю трети

from random import randint

# Создаем список с рандомными целыми числами
my_list = [randint(-100, 100) for i in range(randint(5, 15))]
length = len(my_list)

print(f'Старый список: {my_list}')

# В цикле меняем местами первую и последнюю треть списка
for i in range(int(length / 3)):
    my_list[i], my_list[i - int(length / 3)] = my_list[i - int(length / 3)], my_list[i]

print(f'Измененный список: {my_list}')
