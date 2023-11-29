# Получить с помощью random два случайных числа,
# случайным образом получить арифметическую опрецию,
# совершить операцию над числами и вывести результат

import tkinter
from tkinter import *
from tkinter import ttk
import random


root = Tk()
root.title("Random operations with random numbers")
root.geometry("570x500")
root.resizable(False, False)

sum_sign_num = []
result = 0

def first_number():
    my_first_number = random.random()
    show(my_first_number)
    label_result.config(text=str(my_first_number))
    label1.config(text=str(my_first_number), anchor='center')


def sec_number():
    my_sec_number = random.random()
    label_result.config(text=str(my_sec_number))
    sum_sign_num.append(my_sec_number)
    label2.config(text=str(my_sec_number), anchor='center')

def oper_sign():
    oper_signs = ['+',
                  '-',
                  '*',
                  '/']
    oper_declar = ['need to add ',
                   'need to subtract',
                   'need to multiply',
                   'need to divide']
    dict_oper = dict(zip(oper_declar, oper_signs))
    rand_sign = random.choice(oper_signs)
    label_result.config(text=str(rand_sign))
    show(rand_sign)
    rand_declar = list(filter(lambda key: dict_oper[key] == rand_sign, dict_oper))
    print('I need them ', rand_declar)
    label3.config(text=(rand_declar[0]), anchor='center')
    
def show(value):
    global sum_sign_num
    sum_sign_num.append(value)
    return sum_sign_num
    
def calculate():
    global result
    global sum_sign_num
    label4.config(text='')
    label_result.config(text='')
    if sum_sign_num[2] == '+':
        result = sum_sign_num[0] + sum_sign_num[1]
    elif sum_sign_num[2] == '-':
        result = sum_sign_num[0] - sum_sign_num[1]
    elif sum_sign_num[2] == '*':
        result = sum_sign_num[0] * sum_sign_num[1]
    else:
        result = sum_sign_num[0] / sum_sign_num[1]
   # print('Первое число =', sum_sign_num[0])
    #print('Второе число = ', sum_sign_num[1])
    #print('Результат = ', result)
    label4.config(text=str(result))
    label_result.config(text=str(result))
    
    
def clear_all():
    global result
    global sum_sign_num
    result = 0
    sum_sign_num = []
    label4.config(text='')
    label_result.config(text='')
    label1.config(text='')
    label2.config(text='')
    label3.config(text='')

label_result=Label(root,width=30, height=2, bg='grey', fg='white', text="",font=("arial",15))
label_result.pack()
frm_top = Frame(root, width=10, height=2, bg='lime')
frm_top.pack()

frm_mid = Frame(root,width=10, height=2, bg='yellow')
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
                  command=first_number).pack(side=LEFT, padx=10, pady=10)

btn2 = ttk.Button(frm_top, text='Get the second random number',
                     command=sec_number).pack(side=LEFT, padx=10, pady=10)
    
btn3 = ttk.Button(frm_top, text='What to do with them?',
                      command=oper_sign).pack(side=LEFT, padx=10, pady=10)
btn4 = ttk.Button(root, text='Calculate Button', command=calculate).pack(side=TOP, padx=10, pady=10)

btn5 = ttk.Button(root, text='Clear Button', command=clear_all).pack(side=TOP, padx=10, pady=10)


root.mainloop()