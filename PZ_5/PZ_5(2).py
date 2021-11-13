# функция которая возвращает количество C целых чисел числа K и их сумму S
def digitcountsum(k):
    c = 0
    s = 0
    for i in k:
        c += 1
        s += int(i)
    return c, s


# пример работы функции:
for n in range(5):
    print('Количество цифр: {}. Сумма цифр: {}'.format(*digitcountsum(input('Введите положительное число: '))))
