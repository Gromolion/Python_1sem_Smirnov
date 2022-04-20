from child import *
import sqlite3 as sq


class Main(tk.Frame):
    """Класс для главного окна"""

    def __init__(self, root):
        super().__init__(root)

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

        self.tree.pack()

    def open_dialog_add(self):
        AddChild(self)

    def open_dialog_search(self):
        SearchChild(self)


class DB:
    with sq.connect('BD/saper.db') as con:
        cur = con.cursor()
        cur.execute("DROP TABLE IF EXISTS users")
        cur.execute("""CREATE TABLE IF NOT EXISTS users (
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
    root.mainloop()
