# Удаление дубликатов из отсортированного массива

import random
import numpy as np
class Solution:
    massiv = []
    n = 0
    while n != 15:
        massiv.append(random.randint(2, 20))
        n += 1
    sorted_mass = np.sort(massiv).tolist()
    print(sorted_mass)

    i = 0
    while i <len(sorted_mass)-1:
        if sorted_mass[i] != sorted_mass[i+1]:
            i += 1
        else:
            del sorted_mass[i+1]
    print(sorted_mass)
