import tkinter as tk
import tkinter.ttk as ttk


class AddChild(tk.Toplevel):

    """Класс для дочернего окна"""

    def __init__(self, root):
        super().__init__(root)

        self.title('Добавить игрока')
        self.geometry('400x220+400+300')
        self.resizable(False, False)

        self.label_description = tk.Label(self, text='Номер')
        self.label_description.place(x=50, y=25)
        self.entry_description = ttk.Entry(self)
        self.entry_description.place(x=110, y=25)

        self.label_name = tk.Label(self, text='Имя')
        self.label_name.place(x=50, y=50)
        self.entry_name = ttk.Entry(self)
        self.entry_name.place(x=110, y=50)

        self.label_sex = tk.Label(self, text='Пол')
        self.label_sex.place(x=50, y=75)
        self.combobox = ttk.Combobox(self, values=[u'Мужской', u'Женский'])
        self.combobox.current(0)
        self.combobox.place(x=110, y=75)

        self.label_old = tk.Label(self, text='Возраст')
        self.label_old.place(x=50, y=100)
        self.entry_old = ttk.Entry(self)
        self.entry_old.place(x=110, y=100)

        self.btn_cancel = ttk.Button(self, text='Закрыть', command=self.destroy)
        self.btn_cancel.place(x=300, y=170)

        self.btn_ok = ttk.Button(self, text='Добавить')
        self.btn_ok.place(x=220, y=170)
        self.btn_ok.bind('<Button-1>')

        self.grab_set()
        self.focus_set()


class SearchChild(tk.Toplevel):

    def __init__(self, root):
        super().__init__(root)

        self.title('Найти игрока')
        self.geometry('250x90+400+300')
        self.resizable(False, False)

        self.label_description = tk.Label(self, text='Поиск')
        self.label_description.place(x=20, y=20)
        self.entry_name = ttk.Entry(self)
        self.entry_name.place(x=80, y=20)

        self.btn_search = ttk.Button(self, text='Поиск')
        self.btn_search.place(x=70, y=50)

        self.btn_cancel = ttk.Button(self, text='Отмена', command=self.destroy)
        self.btn_cancel.place(x=150, y=50)
