from tkinter import Tk, Label, Frame, LEFT, TOP
from tkinter import ttk

from lesson_11.app.main import app, root

label_result = Label(root, width=30, height=2, bg='grey', fg='white', text="", font=("arial", 15))
label_result.pack()
frm_top = Frame(root, width=10, height=2, bg='lime')
frm_top.pack()

frm_mid = Frame(root, width=10, height=2, bg='yellow')
frm_mid.pack()

label1 = ttk.Label(frm_mid, width=15, text='Здесь будет первое число', font=12)
label1.pack(side=LEFT, padx=10, pady=10)

label2 = ttk.Label(frm_mid, width=15, text='Здесь будет второе число', font=12)
label2.pack(side=LEFT, padx=10, pady=10)

label3 = ttk.Label(frm_mid, width=15, text='Здесь будет первое число', font=12)
label3.pack(side=LEFT, padx=10, pady=10)

label4 = ttk.Label(root, width=15, text='', font=12)
label4.pack(padx=10, pady=10)

btn1 = ttk.Button(frm_top, text='Get the first random number',
                  command=app.first_number).pack(side=LEFT, padx=10, pady=10)

btn2 = ttk.Button(frm_top, text='Get the second random number',
                  command=app.sec_number).pack(side=LEFT, padx=10, pady=10)

btn3 = ttk.Button(frm_top, text='What to do with them?',
                  command=app.oper_sign).pack(side=LEFT, padx=10, pady=10)
btn4 = ttk.Button(root, text='Calculate Button', command=app.calculate).pack(side=TOP, padx=10, pady=10)

btn5 = ttk.Button(root, text='Clear Button', command=app.clear_all).pack(side=TOP, padx=10, pady=10)
