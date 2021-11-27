voyage = {'Мексика', 'Канада', 'Израиль', 'Италия'}
reynatour = {'Англия', 'Япония', 'Канада', 'ЮАР'}

print('В РейнаТур отсутствуют:', [ i for i in voyage if i not in reynatour])
print('В Вояж отсутствуют:', [i for i in reynatour if i not in voyage])
print('Перечень одинаковых туров:', voyage.intersection(reynatour))
print('Перечни туров', 'равны' if voyage == reynatour else 'неравны')

