from tkinter import *
from tkinter import messagebox, ttk

# --- Функции-обработчики для разных виджетов ---
def on_button_click():
    messagebox.showinfo("Кнопка", "Вы нажали кнопку!")

def on_check():
    state = "включён" if var_check.get() else "выключен"
    label_check.config(text=f"Флажок {state}")

def on_radio():
    selected = var_radio.get()
    label_radio.config(text=f"Выбран вариант {selected}")

def on_listbox_select(event):
    selection = listbox.get(listbox.curselection())
    label_listbox.config(text=f"Выбрано: {selection}")

def on_combobox_select(event):
    label_combobox.config(text=f"Выбрано: {combobox.get()}")

def on_spinbox():
    label_spinbox.config(text=f"Значение: {spinbox.get()}")

def on_scale(val):
    label_scale.config(text=f"Ползунок: {int(float(val))}")

def on_entry_change(event):
    label_entry.config(text=f"Введено: {entry.get()}")

def update_text():
    text_content = text.get("1.0", END)
    label_text.config(text=f"Текст: {text_content[:30]}...")

def on_progress():
    progress['value'] += 10
    if progress['value'] >= 100:
        progress['value'] = 0
    label_progress.config(text=f"Прогресс: {progress['value']}%")

def on_treeview_select(event):
    selected = tree.selection()
    if selected:
        item = tree.item(selected[0])
        label_tree.config(text=f"Выбрано: {item['values'][0]}")

# --- Создание главного окна ---
root = Tk()
root.title("Все виджеты Tkinter")
root.geometry("900x700")

# --- Строка меню ---
menubar = Menu(root)
file_menu = Menu(menubar, tearoff=0)
file_menu.add_command(label="Выход", command=root.quit)
menubar.add_cascade(label="Файл", menu=file_menu)

help_menu = Menu(menubar, tearoff=0)
help_menu.add_command(label="О программе", command=lambda: messagebox.showinfo("О программе", "Демонстрация всех виджетов"))
menubar.add_cascade(label="Справка", menu=help_menu)
root.config(menu=menubar)

# --- Используем Frame для группировки и прокрутки (на случай, если виджетов много) ---
main_frame = Frame(root)
main_frame.pack(fill=BOTH, expand=True)

canvas = Canvas(main_frame)
scrollbar = Scrollbar(main_frame, orient=VERTICAL, command=canvas.yview)
scrollable_frame = Frame(canvas)

scrollable_frame.bind(
    "<Configure>",
    lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
)

canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
canvas.configure(yscrollcommand=scrollbar.set)

canvas.pack(side=LEFT, fill=BOTH, expand=True)
scrollbar.pack(side=RIGHT, fill=Y)

# --- Теперь добавляем виджеты в scrollable_frame, используя grid ---
row = 0
col = 0

# 1. Label
lbl1 = Label(scrollable_frame, text="Привет! Это Label")
lbl1.grid(row=row, column=col, padx=10, pady=5, sticky="w")
row += 1

# 2. Button
btn = Button(scrollable_frame, text="Нажми меня", command=on_button_click)
btn.grid(row=row, column=col, padx=10, pady=5, sticky="w")
row += 1

# 3. Entry (однострочное поле)
entry = Entry(scrollable_frame)
entry.bind("<KeyRelease>", on_entry_change)
entry.grid(row=row, column=col, padx=10, pady=5, sticky="w")
label_entry = Label(scrollable_frame, text="Введено: ")
label_entry.grid(row=row, column=col+1, padx=10, pady=5, sticky="w")
row += 1

# 4. Text (многострочное)
text = Text(scrollable_frame, height=4, width=30)
text.grid(row=row, column=col, padx=10, pady=5, sticky="w")
btn_text = Button(scrollable_frame, text="Обновить метку", command=update_text)
btn_text.grid(row=row, column=col+1, padx=10, pady=5, sticky="w")
label_text = Label(scrollable_frame, text="Текст: ")
label_text.grid(row=row+1, column=col, columnspan=2, padx=10, pady=5, sticky="w")
row += 2

# 5. Checkbutton
var_check = BooleanVar()
check = Checkbutton(scrollable_frame, text="Я согласен", variable=var_check, command=on_check)
check.grid(row=row, column=col, padx=10, pady=5, sticky="w")
label_check = Label(scrollable_frame, text="Флажок выключен")
label_check.grid(row=row, column=col+1, padx=10, pady=5, sticky="w")
row += 1

# 6. Radiobuttons
var_radio = StringVar(value="1")
radio1 = Radiobutton(scrollable_frame, text="Вариант 1", variable=var_radio, value="1", command=on_radio)
radio2 = Radiobutton(scrollable_frame, text="Вариант 2", variable=var_radio, value="2", command=on_radio)
radio1.grid(row=row, column=col, padx=10, pady=5, sticky="w")
radio2.grid(row=row, column=col+1, padx=10, pady=5, sticky="w")
label_radio = Label(scrollable_frame, text="Выбран вариант 1")
label_radio.grid(row=row+1, column=col, columnspan=2, padx=10, pady=5, sticky="w")
row += 2

# 7. Listbox
listbox = Listbox(scrollable_frame, height=3)
listbox.insert(1, "Яблоко")
listbox.insert(2, "Банан")
listbox.insert(3, "Апельсин")
listbox.bind("<<ListboxSelect>>", on_listbox_select)
listbox.grid(row=row, column=col, padx=10, pady=5, sticky="w")
label_listbox = Label(scrollable_frame, text="Выбрано: ")
label_listbox.grid(row=row, column=col+1, padx=10, pady=5, sticky="w")
row += 1

# 8. Combobox (ttk)
combobox = ttk.Combobox(scrollable_frame, values=["Красный", "Зелёный", "Синий"])
combobox.bind("<<ComboboxSelected>>", on_combobox_select)
combobox.grid(row=row, column=col, padx=10, pady=5, sticky="w")
label_combobox = Label(scrollable_frame, text="Выбрано: ")
label_combobox.grid(row=row, column=col+1, padx=10, pady=5, sticky="w")
row += 1

# 9. Spinbox
spinbox = Spinbox(scrollable_frame, from_=0, to=10, command=on_spinbox)
spinbox.grid(row=row, column=col, padx=10, pady=5, sticky="w")
label_spinbox = Label(scrollable_frame, text="Значение: 0")
label_spinbox.grid(row=row, column=col+1, padx=10, pady=5, sticky="w")
row += 1

# 10. Scale (ползунок)
scale = Scale(scrollable_frame, from_=0, to=100, orient=HORIZONTAL, command=on_scale)
scale.grid(row=row, column=col, padx=10, pady=5, sticky="w")
label_scale = Label(scrollable_frame, text="Ползунок: 0")
label_scale.grid(row=row, column=col+1, padx=10, pady=5, sticky="w")
row += 1

# 11. Progressbar (ttk)
progress = ttk.Progressbar(scrollable_frame, length=200, mode='determinate')
progress.grid(row=row, column=col, padx=10, pady=5, sticky="w")
btn_progress = Button(scrollable_frame, text="+10%", command=on_progress)
btn_progress.grid(row=row, column=col+1, padx=10, pady=5, sticky="w")
label_progress = Label(scrollable_frame, text="Прогресс: 0%")
label_progress.grid(row=row+1, column=col, columnspan=2, padx=10, pady=5, sticky="w")
row += 2

# 12. Treeview (таблица)
tree = ttk.Treeview(scrollable_frame, columns=("Имя", "Возраст"), show="headings", height=3)
tree.heading("Имя", text="Имя")
tree.heading("Возраст", text="Возраст")
tree.insert("", "end", values=("Анна", 25))
tree.insert("", "end", values=("Иван", 30))
tree.bind("<<TreeviewSelect>>", on_treeview_select)
tree.grid(row=row, column=col, padx=10, pady=5, sticky="w")
label_tree = Label(scrollable_frame, text="Выбрано: ")
label_tree.grid(row=row, column=col+1, padx=10, pady=5, sticky="w")
row += 1

# 13. Canvas (для рисования)
canvas_widget = Canvas(scrollable_frame, width=200, height=100, bg="white")
canvas_widget.create_rectangle(10, 10, 60, 60, fill="red")
canvas_widget.create_oval(70, 10, 120, 60, fill="blue")
canvas_widget.grid(row=row, column=col, padx=10, pady=5, sticky="w")
Label(scrollable_frame, text="Canvas: фигуры").grid(row=row, column=col+1, padx=10, pady=5, sticky="w")
row += 1

# 14. PanedWindow (простой пример)
paned = PanedWindow(scrollable_frame, orient=HORIZONTAL)
left = Label(paned, text="Левая панель", bg="lightgray")
right = Label(paned, text="Правая панель", bg="lightblue")
paned.add(left)
paned.add(right)
paned.grid(row=row, column=col, columnspan=2, padx=10, pady=5, sticky="ew")
row += 1

# 15. Notebook (вкладки)
notebook = ttk.Notebook(scrollable_frame)
tab1 = Frame(notebook)
tab2 = Frame(notebook)
notebook.add(tab1, text="Вкладка 1")
notebook.add(tab2, text="Вкладка 2")
Label(tab1, text="Содержимое вкладки 1").pack()
Label(tab2, text="Содержимое вкладки 2").pack()
notebook.grid(row=row, column=col, columnspan=2, padx=10, pady=5, sticky="ew")
row += 1

# Запуск
root.mainloop()