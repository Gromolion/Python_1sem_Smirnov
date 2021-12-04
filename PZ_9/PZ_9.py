# программе даны два множества. она должна:
# 1) выводить элементы первого множества, которые отсутствуют во втором
# 2) выводить элементы второго множества, которые отсутствую в первом
# 3) вывести пересекающиеся элементы двух множеств
# 4) вывести, равны ли множества

voyage = {'Мексика', 'Канада', 'Израиль', 'Италия'}
reynatour = {'Англия', 'Япония', 'Канада', 'ЮАР'}

# выводим список элементов Вояж, которые отсутствуют в РейнаТур
print('В РейнаТур отсутствуют:', ", ".join([i for i in voyage if i not in reynatour]))
# выводим список элементов РейнаТур, которые отсутствуют в Вояж
print('В Вояж отсутствуют:', ", ".join([i for i in reynatour if i not in voyage]))
# выводим пересечения множеств Вояж и РейнаТур
print('Перечень одинаковых туров:', *voyage.intersection(reynatour))
# выводим 'равны' если множество Вояж равно множеству РейнаТур, иначе 'неравны'
print('Перечни туров', 'равны' if voyage == reynatour else 'неравны')
