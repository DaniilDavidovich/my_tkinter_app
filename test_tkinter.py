from tkinter import *
from tkinter import messagebox, ttk
from tkinter import filedialog

# --- Функции-обработчики (без изменений) ---
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

def choose_file():
    file_path = filedialog.askopenfilename(title="Выберите файл")
    if file_path:
        label_file.config(text=f"Файл: {file_path}")

def choose_folder():
    folder_path = filedialog.askdirectory(title="Выберите папку")
    if folder_path:
        label_folder.config(text=f"Папка: {folder_path}")

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

# --- Область с прокруткой ---
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

# --- Добавляем виджеты с цветом фона и чёрным текстом ---
row = 0
col = 0

# 1. Label (светло-зелёный)
lbl1 = Label(scrollable_frame, text="Привет! Это Label", bg="#e0ffe0", fg="black")
lbl1.grid(row=row, column=col, padx=10, pady=5, sticky="w")
row += 1

# 2. Button (голубой)
btn = Button(scrollable_frame, text="Нажми меня", command=on_button_click, bg="#a0d6ff", fg="black")
btn.grid(row=row, column=col, padx=10, pady=5, sticky="w")
row += 1

# 3. Entry (жёлтый) + метка
entry = Entry(scrollable_frame, bg="#ffffcc", fg="black")
entry.bind("<KeyRelease>", on_entry_change)
entry.grid(row=row, column=col, padx=10, pady=5, sticky="w")
label_entry = Label(scrollable_frame, text="Введено: ", bg="#ffffcc", fg="black")
label_entry.grid(row=row, column=col+1, padx=10, pady=5, sticky="w")
row += 1

# 4. Text (светло-серый) + кнопка + метка
text = Text(scrollable_frame, height=4, width=30, bg="#f0f0f0", fg="black")
text.grid(row=row, column=col, padx=10, pady=5, sticky="w")
btn_text = Button(scrollable_frame, text="Обновить метку", command=update_text, bg="#a0d6ff", fg="black")
btn_text.grid(row=row, column=col+1, padx=10, pady=5, sticky="w")
label_text = Label(scrollable_frame, text="Текст: ", bg="#f0f0f0", fg="black")
label_text.grid(row=row+1, column=col, columnspan=2, padx=10, pady=5, sticky="w")
row += 2

# 5. Checkbutton (розовый)
var_check = BooleanVar()
check = Checkbutton(scrollable_frame, text="Я согласен", variable=var_check, command=on_check, bg="#ffcccc", fg="black")
check.grid(row=row, column=col, padx=10, pady=5, sticky="w")
label_check = Label(scrollable_frame, text="Флажок выключен", bg="#ffcccc", fg="black")
label_check.grid(row=row, column=col+1, padx=10, pady=5, sticky="w")
row += 1

# 6. Radiobuttons (лавандовый)
var_radio = StringVar(value="1")
radio1 = Radiobutton(scrollable_frame, text="Вариант 1", variable=var_radio, value="1", command=on_radio, bg="#e6ccff", fg="black")
radio2 = Radiobutton(scrollable_frame, text="Вариант 2", variable=var_radio, value="2", command=on_radio, bg="#e6ccff", fg="black")
radio1.grid(row=row, column=col, padx=10, pady=5, sticky="w")
radio2.grid(row=row, column=col+1, padx=10, pady=5, sticky="w")
label_radio = Label(scrollable_frame, text="Выбран вариант 1", bg="#e6ccff", fg="black")
label_radio.grid(row=row+1, column=col, columnspan=2, padx=10, pady=5, sticky="w")
row += 2

# 7. Listbox (оранжевый)
listbox = Listbox(scrollable_frame, height=3, bg="#ffe0b3", fg="black")
listbox.insert(1, "Яблоко")
listbox.insert(2, "Банан")
listbox.insert(3, "Апельсин")
listbox.bind("<<ListboxSelect>>", on_listbox_select)
listbox.grid(row=row, column=col, padx=10, pady=5, sticky="w")
label_listbox = Label(scrollable_frame, text="Выбрано: ", bg="#ffe0b3", fg="black")
label_listbox.grid(row=row, column=col+1, padx=10, pady=5, sticky="w")
row += 1

# 8. Combobox (ttk, цвет фона не меняем, текст чёрный)
combobox = ttk.Combobox(scrollable_frame, values=["Красный", "Зелёный", "Синий"])
combobox.bind("<<ComboboxSelected>>", on_combobox_select)
combobox.grid(row=row, column=col, padx=10, pady=5, sticky="w")
label_combobox = Label(scrollable_frame, text="Выбрано: ", bg="#ccffff", fg="black")
label_combobox.grid(row=row, column=col+1, padx=10, pady=5, sticky="w")
row += 1

# 9. Spinbox (коралловый)
spinbox = Spinbox(scrollable_frame, from_=0, to=10, command=on_spinbox, bg="#ffccb3", fg="black")
spinbox.grid(row=row, column=col, padx=10, pady=5, sticky="w")
label_spinbox = Label(scrollable_frame, text="Значение: 0", bg="#ffccb3", fg="black")
label_spinbox.grid(row=row, column=col+1, padx=10, pady=5, sticky="w")
row += 1

# 10. Scale (серый) – текст метки чёрный
scale = Scale(scrollable_frame, from_=0, to=100, orient=HORIZONTAL, command=on_scale, bg="#cccccc")
scale.grid(row=row, column=col, padx=10, pady=5, sticky="w")
label_scale = Label(scrollable_frame, text="Ползунок: 0", bg="#cccccc", fg="black")
label_scale.grid(row=row, column=col+1, padx=10, pady=5, sticky="w")
row += 1

# 11. Progressbar (метка белая, текст чёрный)
progress = ttk.Progressbar(scrollable_frame, length=200, mode='determinate')
progress.grid(row=row, column=col, padx=10, pady=5, sticky="w")
btn_progress = Button(scrollable_frame, text="+10%", command=on_progress, bg="#a0d6ff", fg="black")
btn_progress.grid(row=row, column=col+1, padx=10, pady=5, sticky="w")
label_progress = Label(scrollable_frame, text="Прогресс: 0%", bg="#ffffff", fg="black")
label_progress.grid(row=row+1, column=col, columnspan=2, padx=10, pady=5, sticky="w")
row += 2

# 12. Treeview (ttk, цвет фона не меняем, текст чёрный)
tree = ttk.Treeview(scrollable_frame, columns=("Имя", "Возраст"), show="headings", height=3)
tree.heading("Имя", text="Имя")
tree.heading("Возраст", text="Возраст")
tree.insert("", "end", values=("Анна", 25))
tree.insert("", "end", values=("Иван", 30))
tree.bind("<<TreeviewSelect>>", on_treeview_select)
tree.grid(row=row, column=col, padx=10, pady=5, sticky="w")
label_tree = Label(scrollable_frame, text="Выбрано: ", bg="#f5f5dc", fg="black")
label_tree.grid(row=row, column=col+1, padx=10, pady=5, sticky="w")
row += 1

# 13. Canvas (белый) – текст метки чёрный
canvas_widget = Canvas(scrollable_frame, width=200, height=100, bg="white")
canvas_widget.create_rectangle(10, 10, 60, 60, fill="red")
canvas_widget.create_oval(70, 10, 120, 60, fill="blue")
canvas_widget.grid(row=row, column=col, padx=10, pady=5, sticky="w")
Label(scrollable_frame, text="Canvas: фигуры", bg="white", fg="black").grid(row=row, column=col+1, padx=10, pady=5, sticky="w")
row += 1

# 14. PanedWindow (светло-серый) – текст внутри Label чёрный
paned = PanedWindow(scrollable_frame, orient=HORIZONTAL, bg="#cccccc")
left = Label(paned, text="Левая панель", bg="lightgray", fg="black")
right = Label(paned, text="Правая панель", bg="lightblue", fg="black")
paned.add(left)
paned.add(right)
paned.grid(row=row, column=col, columnspan=2, padx=10, pady=5, sticky="ew")
row += 1

# 15. Notebook (вкладки) – текст внутри вкладок чёрный (по умолчанию)
notebook = ttk.Notebook(scrollable_frame)
tab1 = Frame(notebook)
tab2 = Frame(notebook)
notebook.add(tab1, text="Вкладка 1")
notebook.add(tab2, text="Вкладка 2")
Label(tab1, text="Содержимое вкладки 1", fg="black").pack()
Label(tab2, text="Содержимое вкладки 2", fg="black").pack()
notebook.grid(row=row, column=col, columnspan=2, padx=10, pady=5, sticky="ew")
row += 1

# 16. Выбор файла и папки (светло-фиолетовый, текст чёрный)
btn_file = Button(scrollable_frame, text="Выбрать файл", command=choose_file, bg="#d9b3ff", fg="black")
btn_file.grid(row=row, column=col, padx=10, pady=5, sticky="w")
label_file = Label(scrollable_frame, text="Файл не выбран", bg="#d9b3ff", fg="black")
label_file.grid(row=row, column=col+1, padx=10, pady=5, sticky="w")
row += 1

btn_folder = Button(scrollable_frame, text="Выбрать папку", command=choose_folder, bg="#d9b3ff", fg="black")
btn_folder.grid(row=row, column=col, padx=10, pady=5, sticky="w")
label_folder = Label(scrollable_frame, text="Папка не выбрана", bg="#d9b3ff", fg="black")
label_folder.grid(row=row, column=col+1, padx=10, pady=5, sticky="w")
row += 1

# Запуск
root.mainloop()