import re
import tkinter as tk
from tkinter import ttk
import sqlite3 as sq


class Main(tk.Frame):
    """Класс для главного окна"""

    def __init__(self, root):
        super().__init__(root)
        self.db = db

        self.toolbar = tk.Frame(bg='#5DD0C0', bd=4)
        self.toolbar.pack(side=tk.TOP, fill=tk.X)

        self.add_img = tk.PhotoImage(file="DB/add.png")
        self.btn_open_dialog = tk.Button(self.toolbar, text='Добавить запись', command=self.open_dialog, bg='#00A08A',
                                         bd=0,
                                         compound=tk.TOP, image=self.add_img)
        self.btn_open_dialog.pack(side=tk.LEFT, padx=20)

        self.update_img = tk.PhotoImage(file="DB/edit.png")
        self.btn_edit_dialog = tk.Button(self.toolbar, text="Редактировать", command=self.open_update_dialog,
                                         bg='#00A08A',
                                         bd=0, compound=tk.TOP, image=self.update_img)
        self.btn_edit_dialog.pack(side=tk.LEFT, padx=20)

        self.delete_img = tk.PhotoImage(file="DB/delete.png")
        self.btn_delete = tk.Button(self.toolbar, text="Удалить запись", command=self.delete_records, bg='#00A08A',
                                    bd=0, compound=tk.TOP, image=self.delete_img)
        self.btn_delete.pack(side=tk.LEFT, padx=20)

        self.search_img = tk.PhotoImage(file="DB/search.png")
        self.btn_search = tk.Button(self.toolbar, text="Поиск записи", command=self.open_search_dialog, bg='#00A08A',
                                    bd=0, compound=tk.TOP, image=self.search_img)
        self.btn_search.pack(side=tk.LEFT, padx=20)

        self.refresh_img = tk.PhotoImage(file="DB/refresh.png")
        self.btn_refresh = tk.Button(self.toolbar, text="Обновить экран", command=self.view_records, bg='#00A08A',
                                     bd=0, compound=tk.TOP, image=self.refresh_img)
        self.btn_refresh.pack(side=tk.LEFT, padx=20)

        self.tree = ttk.Treeview(self, columns=('id', 'patient_name', 'doctor_name', 'diagnosis', 'cost'), height=15,
                                 show='headings')

        self.tree.column('id', width=50, anchor=tk.CENTER)
        self.tree.column('patient_name', width=180, anchor=tk.CENTER)
        self.tree.column('doctor_name', width=140, anchor=tk.CENTER)
        self.tree.column('diagnosis', width=140, anchor=tk.CENTER)
        self.tree.column('cost', width=140, anchor=tk.CENTER)

        self.tree.heading('id', text='ID')
        self.tree.heading('patient_name', text='Имя пациента')
        self.tree.heading('doctor_name', text='Имя доктора')
        self.tree.heading('diagnosis', text='Диагноз')
        self.tree.heading('cost', text='Стоимость')

        self.tree.pack()

        self.view_records()

    def records(self, patient_name, doctor_name, diagnosis, cost):
        self.db.insert_data(patient_name, doctor_name, diagnosis, cost)
        self.view_records()

    def update_record(self, patient_name, doctor_name, diagnosis, cost):
        self.db.cur.execute(
            """UPDATE patients SET patient_name=?, doctor_name=?, diagnosis=?, cost=? WHERE id=?""",
            (patient_name, doctor_name, diagnosis, cost, self.tree.set(self.tree.selection()[0], '#1')))
        self.db.con.commit()
        self.view_records()

    def view_records(self):
        self.db.cur.execute("""SELECT * FROM patients""")
        [self.tree.delete(i) for i in self.tree.get_children()]
        [self.tree.insert('', 'end', values=row) for row in self.db.cur.fetchall()]

    def delete_records(self):
        for selection_item in self.tree.selection():
            self.db.cur.execute("""DELETE FROM patients WHERE id=?""", (self.tree.set(selection_item, '#1'),))
        self.db.con.commit()
        self.view_records()

    def search_records(self, type, cost):
        self.db.cur.execute(f"SELECT * FROM patients WHERE cost {type} {cost}")
        [self.tree.delete(i) for i in self.tree.get_children()]
        [self.tree.insert('', 'end', values=row) for row in self.db.cur.fetchall()]

    def open_dialog(self):
        Child(root, app)

    def open_update_dialog(self):
        self.db.cur.execute("SELECT * FROM patients WHERE id=?",
                            self.tree.set([i for i in self.tree.selection()][0], '#1'))
        Update(self.db.cur.fetchall()[0])

    def open_search_dialog(self):
        Search()


class Child(tk.Toplevel):
    """Класс для дочернего окна"""

    def __init__(self, root, app):
        super().__init__(root)
        self.view = app

        self.title('Добавить пациента')
        self.geometry('400x220+400+300')
        self.resizable(False, False)

        self.label_patient = tk.Label(self, text='Имя пациента')
        self.label_patient.place(x=50, y=50)
        self.entry_patient = ttk.Entry(self)
        self.entry_patient.place(x=140, y=50)

        self.label_doctor = tk.Label(self, text='Имя доктора')
        self.label_doctor.place(x=50, y=75)
        self.entry_doctor = ttk.Entry(self)
        self.entry_doctor.place(x=140, y=75)

        self.label_diagnosis = tk.Label(self, text='Диагноз')
        self.label_diagnosis.place(x=50, y=100)
        self.entry_diagnosis = ttk.Entry(self)
        self.entry_diagnosis.place(x=140, y=100)

        self.label_cost = tk.Label(self, text='Стоимость')
        self.label_cost.place(x=50, y=125)
        self.entry_cost = ttk.Entry(self)
        self.entry_cost.place(x=140, y=125)

        self.btn_cancel = ttk.Button(self, text='Закрыть', command=self.destroy)
        self.btn_cancel.place(x=300, y=170)

        self.btn_ok = ttk.Button(self, text='Добавить')
        self.btn_ok.place(x=220, y=170)
        self.btn_ok.bind('<Button-1>', lambda event: self.view.records(self.entry_patient.get(),
                                                                       self.entry_doctor.get(),
                                                                       self.entry_diagnosis.get(),
                                                                       self.entry_cost.get()))

        self.grab_set()
        self.focus_set()


class Update(Child):
    def __init__(self, fields):
        super().__init__(root, app)
        self.view = app
        self.entry_patient.insert(0, fields[1])
        self.entry_doctor.insert(0, fields[2])
        self.entry_diagnosis.insert(0, fields[3])
        self.entry_cost.insert(0, fields[4])

        self.title("Редактировать запись")
        self.btn_edit = ttk.Button(self, text="Редактировать")
        self.btn_edit.place(x=205, y=170)
        self.btn_edit.bind('<Button-1>', lambda event: self.view.update_record(self.entry_patient.get(),
                                                                               self.entry_doctor.get(),
                                                                               self.entry_diagnosis.get(),
                                                                               self.entry_cost.get()))
        self.btn_ok.destroy()


class Search(tk.Toplevel):
    def __init__(self):
        super().__init__()
        self.view = app

        self.title("Поиск по стоимости")
        self.geometry("300x100+400+300")
        self.resizable(False, False)

        self.label_search = tk.Label(self, text="Стоимость")
        self.label_search.place(x=30, y=20)

        self.search_type = ttk.Combobox(self, values=['=', '>', '<', '>=', '<='], width=3, state='readonly')
        self.search_type.place(x=100, y=20)
        self.search_type.current(1)

        self.entry_search = ttk.Entry(self)
        self.entry_search.place(x=140, y=20, width=150)

        self.btn_search = ttk.Button(self, text="Поиск")
        self.btn_search.place(x=105, y=50)
        self.btn_search.bind('<Button-1>', lambda event: self.view.search_records(self.search_type.get(), self.entry_search.get()))


class DB:
    def __init__(self):
        with sq.connect('DB/polyclinic.db') as self.con:
            self.cur = self.con.cursor()
            self.cur.execute("""CREATE TABLE IF NOT EXISTS patients (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                patient_name TEXT NOT NULL,
                doctor_name TEXT NOT NULL,
                diagnosis TEXT NOT NULL,
                cost INTEGER
                )""")

    def insert_data(self, patient_name, doctor_name, diagnosis, cost):
        self.cur.execute(
            """INSERT INTO patients(patient_name, doctor_name, diagnosis, cost) VALUES (?, ?, ?, ?)""",
            (patient_name, doctor_name, diagnosis, cost))
        self.con.commit()


if __name__ == "__main__":
    root = tk.Tk()
    db = DB()
    app = Main(root)
    app.pack()
    root.title("Платная поликлиника")
    root.geometry("650x450+300+200")
    root.resizable(False, False)
    root.mainloop()
