# В исходном текстовом файле (Dostoevsky.txt) найти все произведения писателя. Посчитать количество полученных элементов
import re

with open('Dostoevsky.txt', 'r') as inp:
    finds = set(re.findall(r'«(.+?)»', inp.read()))
    print(finds)
    print(f'Количество: {len(finds)}')