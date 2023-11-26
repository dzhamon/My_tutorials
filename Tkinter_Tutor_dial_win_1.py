# Диалоговые окна 1/3

from tkinter import *
from tkinter.messagebox import *

root = Tk()

btn1 = Button(root, text='Info', font=('Ubuntu', 20), command=lambda: showinfo('Showinfo', 'Информация'))
btn1.grid(row=0, column=0, sticky='ew')

btn2 = Button(root, text='Warning', font=('Ubuntu', 20), command=lambda: showwarning('Showwarning', 'Предупреждение'))
btn2.grid(row=1, column=0, sticky='ew')

btn3 = Button(root, text='Error', font=('Ubuntu', 20), command=lambda: showerror('Showerror', 'Ошибка'))
btn3.grid(row=2, column=0, sticky='ew')



root.mainloop()