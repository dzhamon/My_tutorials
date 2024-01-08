import random

import numpy as np


def del_dubls(elements):
    sorted_mass = np.sort(elements).tolist()  # list

    # print(sorted_mass)

    i = 0

    while i < len(sorted_mass) - 1:
        if sorted_mass[i] != sorted_mass[i + 1]:
            i += 1
        else:
            del sorted_mass[i + 1]


    # print(sorted_mass)
    return elements


def generate_massiv():
    massiv = []
    n = 0
    while n != 15:
        massiv.append(random.randint(2, 20))
        n += 1
    return massiv

# Алгоритмы # 100%
# Debug (Отладка)
# Журналирование (Logging)
# ctrl + alt + L
# PEP-8
# DRY (Dont repeat yourself) Не повторяй самого себя
# Комбинация alt+enter
# typing.com либо использовать подсказки от Pycharm
# Вместо rev2 закомментировать старый код в том же файле .py
# Использовать кнопку ctrl + ЛКМ для вывода кода и использование объекта в коде
