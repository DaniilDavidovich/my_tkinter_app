from tkinter import *
from tkinter import messagebox, ttk
from tkinter import filedialog

# Funcion
def on_button_click():
    messagebox.showinfo("Button", "Button did tap!")

def on_check():
    state = "on" if var_check.get() else "off"
    label_check.config(text=f"Flag {state}")

def on_radio():
    selected = var_radio.get()
    label_radio.config(text=f"Selected: {selected}")

def on_listbox_select(event):
    selection = listbox.get(listbox.curselection())
    label_listbox.config(text=f"Selected: {selection}")

def on_combobox_select(event):
    label_combobox.config(text=f"Selected: {combobox.get()}")

def on_spinbox():
    label_spinbox.config(text=f"Value: {spinbox.get()}")

def on_scale(val):
    label_scale.config(text=f"Slider: {int(float(val))}")

def on_entry_change(event):
    label_entry.config(text=f"Entered: {entry.get()}")

def update_text():
    text_content = text.get("1.0", END)
    label_text.config(text=f"Text: {text_content[:30]}...")

def on_progress():
    progress['value'] += 10
    if progress['value'] >= 100:
        progress['value'] = 0
    label_progress.config(text=f"Pregress: {progress['value']}%")

def on_treeview_select(event):
    selected = tree.selection()
    if selected:
        item = tree.item(selected[0])
        label_tree.config(text=f"Selected: {item['values'][0]}")

def choose_file():
    file_path = filedialog.askopenfilename(title="Select File")
    if file_path:
        label_file.config(text=f"File: {file_path}")

def choose_folder():
    folder_path = filedialog.askdirectory(title="Select Folder")
    if folder_path:
        label_folder.config(text=f"Folder: {folder_path}")

# Main
root = Tk()
root.title("widgets Tkinter")
root.geometry("900x700")

# Menu
menubar = Menu(root)
file_menu = Menu(menubar, tearoff=0)
file_menu.add_command(label="Close program", command=root.quit)
menubar.add_cascade(label="File", menu=file_menu)
help_menu = Menu(menubar, tearoff=0)
help_menu.add_command(label="About", command=lambda: messagebox.showinfo("About", "Widgets"))
menubar.add_cascade(label="Info", menu=help_menu)
root.config(menu=menubar)

# Scroll
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


row = 0
col = 0

# 1. Label
lbl1 = Label(scrollable_frame, text="Hi! Its Label", bg="#e0ffe0", fg="black")
lbl1.grid(row=row, column=col, padx=10, pady=5, sticky="w")
row += 1

# 2. Button
btn = Button(scrollable_frame, text="Press me", command=on_button_click, bg="#a0d6ff", fg="black")
btn.grid(row=row, column=col, padx=10, pady=5, sticky="w")
row += 1

# 3. Entry 
entry = Entry(scrollable_frame, bg="#ffffcc", fg="black")
entry.bind("<KeyRelease>", on_entry_change)
entry.grid(row=row, column=col, padx=10, pady=5, sticky="w")
label_entry = Label(scrollable_frame, text="Entered Text: ", bg="#ffffcc", fg="black")
label_entry.grid(row=row, column=col+1, padx=10, pady=5, sticky="w")
row += 1

# 4. Text 
text = Text(scrollable_frame, height=4, width=30, bg="#f0f0f0", fg="black")
text.grid(row=row, column=col, padx=10, pady=5, sticky="w")
btn_text = Button(scrollable_frame, text="Update", command=update_text, bg="#a0d6ff", fg="black")
btn_text.grid(row=row, column=col+1, padx=10, pady=5, sticky="w")
label_text = Label(scrollable_frame, text="Text: ", bg="#f0f0f0", fg="black")
label_text.grid(row=row+1, column=col, columnspan=2, padx=10, pady=5, sticky="w")
row += 2

# 5. Checkbutton 
var_check = BooleanVar()
check = Checkbutton(scrollable_frame, text="Flag", variable=var_check, command=on_check, bg="#ffcccc", fg="black")
check.grid(row=row, column=col, padx=10, pady=5, sticky="w")
label_check = Label(scrollable_frame, text="Flag is off", bg="#ffcccc", fg="black")
label_check.grid(row=row, column=col+1, padx=10, pady=5, sticky="w")
row += 1

# 6. Radiobuttons 
var_radio = StringVar(value="1")
radio1 = Radiobutton(scrollable_frame, text="Option 1", variable=var_radio, value="1", command=on_radio, bg="#e6ccff", fg="black")
radio2 = Radiobutton(scrollable_frame, text="Option 2", variable=var_radio, value="2", command=on_radio, bg="#e6ccff", fg="black")
radio1.grid(row=row, column=col, padx=10, pady=5, sticky="w")
radio2.grid(row=row, column=col+1, padx=10, pady=5, sticky="w")
label_radio = Label(scrollable_frame, text="Selected option 1", bg="#e6ccff", fg="black")
label_radio.grid(row=row+1, column=col, columnspan=2, padx=10, pady=5, sticky="w")
row += 2

# 7. Listbox 
listbox = Listbox(scrollable_frame, height=3, bg="#ffe0b3", fg="black")
listbox.insert(1, "Apple")
listbox.insert(2, "Banana")
listbox.insert(3, "Orange")
listbox.bind("<<ListboxSelect>>", on_listbox_select)
listbox.grid(row=row, column=col, padx=10, pady=5, sticky="w")
label_listbox = Label(scrollable_frame, text="Selected: ", bg="#ffe0b3", fg="black")
label_listbox.grid(row=row, column=col+1, padx=10, pady=5, sticky="w")
row += 1

# 8. Combobox (ttk)
combobox = ttk.Combobox(scrollable_frame, values=["Red", "Green", "Blue"])
combobox.bind("<<ComboboxSelected>>", on_combobox_select)
combobox.grid(row=row, column=col, padx=10, pady=5, sticky="w")
label_combobox = Label(scrollable_frame, text="Selected: ", bg="#ccffff", fg="black")
label_combobox.grid(row=row, column=col+1, padx=10, pady=5, sticky="w")
row += 1

# 9. Spinbox
spinbox = Spinbox(scrollable_frame, from_=0, to=10, command=on_spinbox, bg="#ffccb3", fg="black")
spinbox.grid(row=row, column=col, padx=10, pady=5, sticky="w")
label_spinbox = Label(scrollable_frame, text="Value: 0", bg="#ffccb3", fg="black")
label_spinbox.grid(row=row, column=col+1, padx=10, pady=5, sticky="w")
row += 1

# 10. Scale 
scale = Scale(scrollable_frame, from_=0, to=100, orient=HORIZONTAL, command=on_scale, bg="#cccccc")
scale.grid(row=row, column=col, padx=10, pady=5, sticky="w")
label_scale = Label(scrollable_frame, text="Slider: 0", bg="#cccccc", fg="black")
label_scale.grid(row=row, column=col+1, padx=10, pady=5, sticky="w")
row += 1

# 11. Progressbar
progress = ttk.Progressbar(scrollable_frame, length=200, mode='determinate')
progress.grid(row=row, column=col, padx=10, pady=5, sticky="w")
btn_progress = Button(scrollable_frame, text="+10%", command=on_progress, bg="#a0d6ff", fg="black")
btn_progress.grid(row=row, column=col+1, padx=10, pady=5, sticky="w")
label_progress = Label(scrollable_frame, text="Progress: 0%", bg="#ffffff", fg="black")
label_progress.grid(row=row+1, column=col, columnspan=2, padx=10, pady=5, sticky="w")
row += 2

# 12. Treeview (ttk)
tree = ttk.Treeview(scrollable_frame, columns=("Name", "Age"), show="headings", height=3)
tree.heading("Name", text="Name")
tree.heading("Age", text="Name")
tree.insert("", "end", values=("Anna", 25))
tree.insert("", "end", values=("Vladislav", 30))
tree.bind("<<TreeviewSelect>>", on_treeview_select)
tree.grid(row=row, column=col, padx=10, pady=5, sticky="w")
label_tree = Label(scrollable_frame, text="Выбрано: ", bg="#f5f5dc", fg="black")
label_tree.grid(row=row, column=col+1, padx=10, pady=5, sticky="w")
row += 1

# 13. Canvas
canvas_widget = Canvas(scrollable_frame, width=200, height=100, bg="white")
canvas_widget.create_rectangle(10, 10, 60, 60, fill="red")
canvas_widget.create_oval(70, 10, 120, 60, fill="blue")
canvas_widget.grid(row=row, column=col, padx=10, pady=5, sticky="w")
Label(scrollable_frame, text="Canvas: shapes", bg="white", fg="black").grid(row=row, column=col+1, padx=10, pady=5, sticky="w")
row += 1

# 14. PanedWindow
paned = PanedWindow(scrollable_frame, orient=HORIZONTAL, bg="#cccccc")
left = Label(paned, text="Left panel", bg="lightgray", fg="black")
right = Label(paned, text="Right panel", bg="lightblue", fg="black")
paned.add(left)
paned.add(right)
paned.grid(row=row, column=col, columnspan=2, padx=10, pady=5, sticky="ew")
row += 1

# 15. Notebook
notebook = ttk.Notebook(scrollable_frame)
tab1 = Frame(notebook)
tab2 = Frame(notebook)
notebook.add(tab1, text="Page 1")
notebook.add(tab2, text="Page 2")
Label(tab1, text="Content 1", fg="black").pack()
Label(tab2, text="Сontent 2", fg="black").pack()
notebook.grid(row=row, column=col, columnspan=2, padx=10, pady=5, sticky="ew")
row += 1

# 16. Select file and folder
btn_file = Button(scrollable_frame, text="Select file", command=choose_file, bg="#d9b3ff", fg="black")
btn_file.grid(row=row, column=col, padx=10, pady=5, sticky="w")
label_file = Label(scrollable_frame, text="File not selected", bg="#d9b3ff", fg="black")
label_file.grid(row=row, column=col+1, padx=10, pady=5, sticky="w")
row += 1

btn_folder = Button(scrollable_frame, text="Select folder", command=choose_folder, bg="#d9b3ff", fg="black")
btn_folder.grid(row=row, column=col, padx=10, pady=5, sticky="w")
label_folder = Label(scrollable_frame, text="Folder not selected", bg="#d9b3ff", fg="black")
label_folder.grid(row=row, column=col+1, padx=10, pady=5, sticky="w")
row += 1

# Start
root.mainloop()