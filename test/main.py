from child import *
import sqlite3 as sq


class Main(tk.Frame):
    """Класс для главного окна"""

    def __init__(self, root):
        super().__init__(root)

        self.db = DB()

        self.toolbar = tk.Frame(bg='#a0dea0', bd=4)
        self.toolbar.pack(side=tk.TOP, fill=tk.X)

        self.add_img = tk.PhotoImage(file='BD/add.png')
        self.btn_open_dialog_add = tk.Button(self.toolbar, text='Добавить игрока', command=self.open_dialog_add,
                                             bg='#5da130', bd=0, compound=tk.TOP, image=self.add_img)
        self.btn_open_dialog_add.pack(side=tk.LEFT)

        self.search_img = tk.PhotoImage(file='BD/search.png')
        self.btn_open_dialog_search = tk.Button(self.toolbar, text='Найти игрока', command=self.open_dialog_search,
                                                bg='#5da130', bd=0, compound=tk.TOP, image=self.search_img)
        self.btn_open_dialog_search.pack(side=tk.LEFT, padx=5)

        self.refresh_img = tk.PhotoImage(file='BD/refresh.png')
        self.btn_open_dialog_refresh = tk.Button(self.toolbar, text='Обновить', command=self.open_dialog_refresh,
                                                 bg='#5da130', bd=0, compound=tk.TOP, image=self.refresh_img)
        self.btn_open_dialog_refresh.pack(side=tk.RIGHT)

        self.tree = ttk.Treeview(self, columns=('user_id', 'name', 'sex', 'old', 'score'), height=15, show='headings')

        self.tree.column('user_id', width=50, anchor=tk.CENTER)
        self.tree.column('name', width=180, anchor=tk.CENTER)
        self.tree.column('sex', width=140, anchor=tk.CENTER)
        self.tree.column('old', width=140, anchor=tk.CENTER)
        self.tree.column('score', width=140, anchor=tk.CENTER)

        self.tree.heading('user_id', text='ID')
        self.tree.heading('name', text='Имя игрока')
        self.tree.heading('sex', text='Пол игрока')
        self.tree.heading('old', text='Возраст игрока')
        self.tree.heading('score', text='Результат игрока')

        ysb = ttk.Scrollbar(self, orient=tk.VERTICAL, command=self.tree.yview)
        self.tree.configure(yscroll=ysb.set)

        self.db.cur.execute('SELECT * FROM users')
        self.iid = 1
        for row in self.db.cur.fetchall():
            self.tree.insert('', 'end', values=row, iid=str(self.iid))
            self.iid += 1
            self.tree.bind('<<Double-Button-1>>', self.player_update)

        self.tree.pack()

    def player_update(self, a):
        print(1)

    def open_dialog_add(self):
        AddChild(self, self.db.con)
        self.open_dialog_refresh()

    def open_dialog_search(self):
        SearchChild(self, self.db.con)

    def open_dialog_refresh(self):
        [self.tree.delete(i) for i in self.tree.get_children()]
        self.db.cur.execute('SELECT * FROM users')
        self.iid = 1
        for row in self.db.cur.fetchall():
            self.tree.insert('', 'end', values=row, iid=str(self.iid))
            self.iid += 1


class DB:
    def __init__(self):
        with sq.connect('BD/saper.db') as con:
            self.con = con
            self.cur = con.cursor()
            self.cur.execute("""CREATE TABLE IF NOT EXISTS users (
            user_id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            sex INTEGER NOT NULL DEFAULT 1,
            old INTEGER,
            score INTEGER
            )""")


if __name__ == '__main__':
    root = tk.Tk()
    app = Main(root)
    app.pack()
    root.title('Работа с базой данных Сапер')
    root.geometry('650x450+300+200')
    root.resizable(False, False)
    root.after(1000, app.update)
    root.mainloop()
