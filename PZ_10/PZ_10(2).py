# Из предложенного файла(text18-25.txt) вывести на экран его содержимое, количество символов,
# принадлежащих к группе букв. Сформировать новый файл, в который поместить текст в стихотворной форме,
# предварительно удалив букву с из текста.
with open('text18-25.txt', 'r', encoding='utf-16') as inp:
    content = inp.read()
    print(content)
    sum_alph = len([i for i in content if i.isalpha()])
    print(f'Количество букв: {sum_alph}')
with open('result2.txt', 'w') as r:
    r.write(content.replace('с', ''))
