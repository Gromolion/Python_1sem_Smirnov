# Программа формирует два файла (.txt), содержащих по одной последовательности из целых положительных
# и отрицательных чисел. Затем формирует новый текстовый файл (.txt), следующего вида:
# Элементы первого и второго файлов:
# Элементы после сортировки:
# Количество элементов:
# Минимальный элемент, кратный 2:
# Максимальный элемент, кратный 5:

from random import randint

if input('Сгенерировать файлы заново? ').upper() == 'Да'.upper():
    with open('first.txt', 'w') as f:
        buff = [randint(-1000, 1000) for i in range(randint(1, 20))]
        line = ''
        for i in buff:
            line += str(i) + ' '
        f.write(line)
    # создаю первый файл с рандомной последовательностью чисел от -100 от 100
    with open('second.txt', 'w') as f:
        buff = [randint(-1000, 1000) for i in range(randint(1, 20))]
        line = ''
        for i in buff:
            line += str(i) + ' '
        f.write(line)
    # создаю второй файл с рандомной последовательностью чисел от -100 от 100
with open('result.txt', 'w') as r:
    with open('first.txt', 'r') as f1, open('second.txt', 'r') as f2:
        buff = f1.readline().split() + f2.readline().split()
        # с помощью split() преобразовываю строки из первого и второго файлов в списки и соединяю их
        line = ''
        for i in buff:
            line += i + ' '
        # преобразую список в строку
        r.write(f'Элементы первого и второго файлов:\n{line}\n')
        line = ''
        for i in sorted(buff):
            line += i + ' '
        # преобразую сортированный список в строку
        r.write(f'Элементы после сортировки:\n{line}\n')
        r.write(f'Количество элементов: {len(buff)}\n')
        r.write(f'Минимальный элемент кратный 2: {min([i for i in buff if int(i) % 2 == 0])}\n')
        # создаю список из элементов buff, кратных 2, и нахожу минимальный из них
        r.write(f'Максимальный элемент кратный 5: {max([i for i in buff if int(i) % 5 == 0])}')
        # создаю список из элементов buff, кратных 5, и нахожу максимальный из них
