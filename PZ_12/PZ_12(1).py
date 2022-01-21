# В соответствии с номером варианта перейти по ссылке на прототип. Реализовать
# его в IDE PyCharm Community с применением пакета tk. Получить интерфейс
# максимально приближенный к оригиналу (см. таблицу 1).

from tkinter import *

root = Tk()
root.title('Форма заявки')
root.geometry('550x470+500+100')
root.resizable(0, 0)
root.configure(background='white')

# создаю экземпляры объектов рамок, текста, кнопок и текстовых полей
frame1 = Frame(highlightthickness=1,
               highlightbackground="#64D8D1",
               width=506,
               height=24,
               )
label1 = Label(text='Форма заявки',
               font='Aerial 12 bold',
               fg='white',
               bg='#3F9D65')

frame2 = Frame(highlightthickness=1,
               bg='#E9E4E4',
               highlightbackground="#64D8D1",
               width=506,
               height=64)
label2_1 = Label(text='Допустимые типы вложений:',
                 font='Aerial 8 bold',
                 bg='#E9E4E4')
label2_2 = Label(text='zip, rar, txt, doc, jpg, png, gif, odt, xml',
                 font='Aerial 8',
                 bg='#E9E4E4')
label2_3 = Label(text='Макс. размер каждого файла:',
                 font='Aerial 8 bold',
                 bg='#E9E4E4')
label2_4 = Label(text='1024kb.',
                 font='Aerial 8',
                 bg='#E9E4E4')
label2_5 = Label(text='Макс. общий размер файла:',
                 font='Aerial 8 bold',
                 bg='#E9E4E4')
label2_6 = Label(text='2048kb.',
                 font='Aerial 8',
                 bg='#E9E4E4')

frame3 = Frame(highlightthickness=1,
               bg='#E9E4E4',
               highlightbackground="#64D8D1",
               width=153,
               height=28)
label3 = Label(text='Ваше имя:',
               bg='#E9E4E4',
               font='Aerial 12')

frame4 = Frame(highlightthickness=1,
               bg='#E9E4E4',
               highlightbackground="#64D8D1",
               width=153,
               height=28)
label4 = Label(text='Ваш email:',
               bg='#E9E4E4',
               font='Aerial 12')

frame5 = Frame(highlightthickness=1,
               bg='#E9E4E4',
               highlightbackground="#64D8D1",
               width=153,
               height=28)
label5 = Label(text='Тема письма:',
               bg='#E9E4E4',
               font='Aerial 12')

frame6 = Frame(highlightthickness=1,
               bg='#E9E4E4',
               highlightbackground="#64D8D1",
               width=153,
               height=28)
label6 = Label(text='Прикрепить файл:',
               bg='#E9E4E4',
               font='Aerial 12')

frame7 = Frame(highlightthickness=1,
               bg='#E9E4E4',
               highlightbackground="#64D8D1",
               width=153,
               height=28)
label7 = Label(text='Прикрепить файл:',
               bg='#E9E4E4',
               font='Aerial 12')

frame8 = Frame(highlightthickness=1,
               bg='#E9E4E4',
               highlightbackground="#64D8D1",
               width=153,
               height=28)
label8 = Label(text='Прикрепить файл:',
               bg='#E9E4E4',
               font='Aerial 12')

frame9 = Frame(highlightthickness=1,
               bg='#E9E4E4',
               highlightbackground="#64D8D1",
               width=354,
               height=28)
entry9 = Entry()
label9 = Label(text='*', font='Aerial 25', fg='red', bg='#E9E4E4')

frame10 = Frame(highlightthickness=1,
                bg='#E9E4E4',
                highlightbackground="#64D8D1",
                width=354,
                height=28)
entry10 = Entry()
label10 = Label(text='*', font='Aerial 25', fg='red', bg='#E9E4E4')

frame11 = Frame(highlightthickness=1,
                bg='#E9E4E4',
                highlightbackground="#64D8D1",
                width=354,
                height=28)
entry11 = Entry()

frame12 = Frame(highlightthickness=1,
                bg='#E9E4E4',
                highlightbackground="#64D8D1",
                width=354,
                height=28)
entry12 = Entry()
button12 = Button(text='Обзор...', justify='center', font='Aerial 8', relief='raised')

frame13 = Frame(highlightthickness=1,
                bg='#E9E4E4',
                highlightbackground="#64D8D1",
                width=354,
                height=28)
entry13 = Entry()
button13 = Button(text='Обзор...', justify='center', font='Aerial 8', relief='raised')

frame14 = Frame(highlightthickness=1,
                bg='#E9E4E4',
                highlightbackground="#64D8D1",
                width=354,
                height=28)
entry14 = Entry()
button14 = Button(text='Обзор...', justify='center', font='Aerial 8', relief='raised')

frame15 = Frame(highlightthickness=1,
                bg='#E9E4E4',
                highlightbackground="#64D8D1",
                width=506,
                height=154)
label15_1 = Label(text='Ваше сообщение:',
                  font='Aerial 12',

                  bg='#E9E4E4')
label15_2 = Label(text='*', font='Aerial 25', fg='red', bg='#E9E4E4')
text15 = Text()

frame16 = Frame(highlightthickness=1,
                highlightbackground="#64D8D1",
                bg='#3F9D65',
                width=506,
                height=30)
button16_1 = Button(text='Отправить Email', font='Aerial 10')
button16_2 = Button(text='Очистить', font='Aerial 10')

# размещаю рамки в интерфейсе
frame1.place(x=20, y=16)
frame2.place(x=20, y=39)
frame3.place(x=20, y=102)
frame9.place(x=172, y=102)
frame4.place(x=20, y=129)
frame10.place(x=172, y=129)
frame5.place(x=20, y=156)
frame11.place(x=172, y=156)
frame6.place(x=20, y=183)
frame12.place(x=172, y=183)
frame7.place(x=20, y=210)
frame13.place(x=172, y=210)
frame8.place(x=20, y=237)
frame14.place(x=172, y=237)
frame15.place(x=20, y=263)
frame16.place(x=20, y=416)

# размещаю текст в интерфейсе
label1.place(x=21, y=17, width=504, height=22)
label2_1.place(x=21, y=45, width=180, height=18)
label2_2.place(x=200, y=45)
label2_3.place(x=21, y=63, width=180, height=18)
label2_4.place(x=200, y=63)
label2_5.place(x=21, y=81, width=170, height=18)
label2_6.place(x=190, y=81)
label3.place(x=25, y=104)
label4.place(x=25, y=131)
label5.place(x=25, y=158)
label6.place(x=25, y=185)
label7.place(x=25, y=212)
label8.place(x=25, y=239)
label9.place(x=383, y=106, height=25)
label10.place(x=383, y=135, height=25)
label15_1.place(x=25, y=265)
label15_2.place(x=158, y=269, height=25)

# размещаю поля ввода текста
entry9.place(x=177, y=106, width=205)
entry10.place(x=177, y=135, width=205)
entry11.place(x=177, y=160, width=205)
entry12.place(x=177, y=187, width=205)
entry13.place(x=177, y=214, width=205)
entry14.place(x=177, y=241, width=205)
text15.place(x=56, y=288, width=436, height=120)

# размещаю кнопки
button12.place(x=385, y=187, height=21)
button13.place(x=385, y=214, height=21)
button14.place(x=385, y=241, height=21)
button16_1.place(x=160, y=421, height=21, width=120)
button16_2.place(x=290, y=421, height=21, width=80)

# запускаю цикл работы программы
root.mainloop()
