# Получить с помощью random два случайных числа,
# случайным образом получить арифметическую опрецию,
# совершить операцию над числами и вывести результат

from tkinter import *

import random

from calculator import label_result
from my_first_task import label1, label2, label3

root = Tk()
root.title("Random operations with random numbers")
root.geometry("570x500")
root.resizable(False, False)


class MyApp:
    sum_sign_num = []
    result = 0

    def first_number(self):
        my_first_number = random.randint(5, 250)
        self.show(str(my_first_number))
        label_result.config(text=str(my_first_number))
        label1.config(text=str(my_first_number), anchor='center')

    def sec_number(self):
        my_sec_number = random.randint(5, 250)
        label_result.config(text=str(my_sec_number))
        self.sum_sign_num.append(my_sec_number)
        label2.config(text=str(my_sec_number), anchor='center')

    def oper_sign(self):
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
        self.show(rand_sign)
        rand_declar = list(filter(lambda key: dict_oper[key] == rand_sign, dict_oper))
        print('I need them ', rand_declar)
        label3.config(text=(rand_declar[0]), anchor='center')

    def show(self, value):
        self.sum_sign_num.append(value)
        return self.sum_sign_num

    def calculate(self):
        label4.config(text='')
        label_result.config(text='')
        calc_str = (str(self.sum_sign_num[0])+str(self.sum_sign_num[2])+str(self.sum_sign_num[1]))
        self.result = eval(calc_str)
        # print('Результат = ', result)
        label4.config(text=str(self.result))
        label_result.config(text=str(self.result))

    def clear_all(self):
        self.result = 0
        self.sum_sign_num = []
        label4.config(text='')
        label_result.config(text='')
        label1.config(text='')
        label2.config(text='')
        label3.config(text='')


app = MyApp()
root.mainloop()
