# разработать программу с применением пакета tk, взяв в качестве условия
# одну любую задачу из ПЗ №3-8.

from test import *
from test import messagebox


def show_msg():
    # функция отображения результата
    try:
        x = int(inp_x.get())
        y = int(inp_y.get())

    except ValueError:
        messagebox.showerror("Ошибка", 'Одно из введенных значений не является числом')

    else:
        result = 'лежит' if x < 0 < y else 'не лежит'
        messagebox.showinfo('Вывод', f'Точка с заданными координатами {result} во второй четверти')


root = Tk()
root.title('ПЗ_3_1')
root.geometry('600x300+400+100')
root['bg'] = '#B0E0E6'


cond = Label(text='Программа для проверки, лежит ли точка\n с заданными координатами во второй четверти',
             font='Aerial 14 bold', bg='#B0E0E6', pady=15)
cond.pack()

frame = Frame(pady=10, padx=10, bg='#B0E0E6')
frame.pack(fill='x')
txt_x = Label(frame, text='Введите x:', font='Aerial 12', bg='#B0E0E6')
inp_x = Entry(frame, bg='lightgreen')
txt_x.pack(side='left')
inp_x.pack(side='left')

txt_y = Label(frame, text='Введите y:', font='Aerial 12', bg='#B0E0E6')
inp_y = Entry(frame, bg='lightgreen')
inp_y.pack(side='right')
txt_y.pack(side='right')

# кнопка, которая при нажатия вызывает функцию show_msg
button = Button(text='Получить ответ', bg='lightgreen', command=show_msg)
button.pack()


root.mainloop()
