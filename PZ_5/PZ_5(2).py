# функция которая возвращает количество C целых чисел числа K и их сумму S
def digitcountsum(k):
    c = 0
    s = 0
    for i in k:
        c += 1
        s += int(i)
    return c, s


for n in range(5):
    number = input('Введите положительное число: ')
    print('Количество цифр: {}. Сумма цифр: {}'.format(*digitcountsum(number)))
    # в каждой итерации цикла мы выводим форматированную строку со значениями, которые вернула функция digitcountsum()
