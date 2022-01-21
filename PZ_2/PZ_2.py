# программа выводит на экран последовательность целых чисел от a до b(включая b) и количество этих чисел
a, b = input('Введите целые цисла a и b (a < b): ').split()

while type(a) != int or type(b) != int or a > b:
    # обработка исключений
    try:
        a = int(a)
        b = int(b)

        if a > b:
            print('a > b')
            a, b = input('Введите a и b заново: ').split()

    except ValueError:
        print('a или b не целые цисла')
        a, b = input('Введите a и b заново: ').split()

c = 0
for i in range(a, b + 1):
    # выводит на экран числа в порядке возрастания от a до b(включая b), попутно считая количество этих чисел
    print(i)
    c += 1

print(f'Количество чисел: {c}')

# способ через while:

# n = 0
# while a <= b:
#     print(a)
#     a += 1
#     n += 1
# print(f'Количество чисел: {n}')

# print(*range(a, b + 1), '\nКоличество чисел:', len(range(a, b + 1)))
# *range(a, b + 1) создает и сразу же распаковывает список чисел от a до b(включая b)
# len(range(a, b + 1)) возвращает количество чисел от a до b(включая b)

# print('', *[str(i) + '\n' for i in range(a, b + 1)], f'\nКоличество чисел: {len(range(a, b + 1))}')
# n = 0
# while a <= b:
#     print(a)
#     a += 1
#     n += 1
# print(f'Количество чисел: {n}')
