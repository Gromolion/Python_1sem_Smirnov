import tkinter as tk
import tkinter.ttk as ttk


class AddChild(tk.Toplevel):

    """Класс для дочернего окна"""

    def __init__(self, root, con):
        super().__init__(root)

        self.con = con

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

        self.label_score = tk.Label(self, text='Результат')
        self.label_score.place(x=50, y=125)
        self.entry_score = ttk.Entry(self)
        self.entry_score.place(x=110, y=125)

        self.btn_cancel = ttk.Button(self, text='Закрыть', command=self.destroy)
        self.btn_cancel.place(x=300, y=170)

        self.btn_ok = ttk.Button(self, text='Добавить', command=self.add)
        self.btn_ok.place(x=220, y=170)
        self.btn_ok.bind('<Button-1>')

        self.grab_set()
        self.focus_set()

    def add(self):
        cur = self.con.cursor()
        number = self.entry_description.get()
        name = self.entry_name.get()
        sex = self.combobox.current()
        old = self.entry_old.get()
        score = self.entry_score.get()
        cur.execute(f"INSERT INTO users VALUES ({number}, '{name}', {sex}, {old}, {score})")
        self.con.commit()


class UpdateChild(AddChild):
    def __init__(self, root, con, app):
        super(UpdateChild, self).__init__(root, con)
        self.app = app
        self.title('Редактировать запись')
        self.btn_edit = ttk.Button(self, text="Редактировать")
        self.btn_edit.place(x=205, y=170)
        self.btn_edit.bind('<Button-1>', lambda event: self.update())
        self.btn_ok.destroy()

    def update(self):
        self.app.update(self.entry_description.get(),
                        self.entry_name.get(),
                        self.combobox.get(),
                        self.entry_old.get(),
                        self.entry_score.get())
        self.app.refresh()
        self.destroy()


class SearchChild(tk.Toplevel):

    def __init__(self, root, con):
        super().__init__(root)

        self.con = con

        self.title('Найти игрока')
        self.geometry('220x90+400+300')
        self.resizable(False, False)

        self.label_description = tk.Label(self, text='Поиск')
        self.label_description.place(x=20, y=20)
        self.entry_name = ttk.Entry(self)
        self.entry_name.place(x=80, y=20)

        self.btn_search = ttk.Button(self, text='Поиск', command=self.search)
        self.btn_search.place(x=60, y=50)

        self.btn_cancel = ttk.Button(self, text='Отмена', command=self.destroy)
        self.btn_cancel.place(x=140, y=50)

    def search(self):
        cur = self.con.cursor()
        data = self.entry_name.get()
        cur.execute(f"SELECT * FROM users WHERE name LIKE '%{data}%'")
        users = cur.fetchall()

        self.geometry('400x150+400+300')

        self.entry_name.destroy()
        self.label_description.destroy()
        self.btn_search.destroy()
        self.btn_cancel.destroy()

        tree = ttk.Treeview(self, columns=('user_id', 'name', 'sex', 'old', 'score'), height=4, show='headings')
        tree.column('user_id', width=25, anchor=tk.CENTER)
        tree.column('name', width=89, anchor=tk.CENTER)
        tree.column('sex', width=87, anchor=tk.CENTER)
        tree.column('old', width=95, anchor=tk.CENTER)
        tree.column('score', width=102, anchor=tk.CENTER)
        tree.heading('user_id', text='ID')
        tree.heading('name', text='Имя игрока')
        tree.heading('sex', text='Пол игрока')
        tree.heading('old', text='Возраст игрока')
        tree.heading('score', text='Результат игрока')
        tree.pack()

        for row in users:
            tree.insert('', 'end', values=row)

        btn_quit = ttk.Button(self, text='Выйти', command=self.destroy)
        btn_quit.place(x=300, y=110)

