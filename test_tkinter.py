from tkinter import *
from tkinter import messagebox

# Классы с параметрами
label_x = 10
label_y = 10
button_x = 100
button_y = 200

# Функция-обработчик
def clicked():
    messagebox.showinfo('Заголовок', 'текст')

# Основная часть — создание окна и виджетов
if __name__ == '__main__':
    root = Tk()
    root.title('My App')
    root.geometry('400x400')

    lbl1 = Label(root, text='Привет!')
    btn1 = Button(root, text='Не нажимай', command=clicked)

    # Размещение с использованием параметров из классов
    lbl1.place(x=label_x, y=label_y)
    btn1.place(x=button_x, y=button_y)

    root.mainloop()