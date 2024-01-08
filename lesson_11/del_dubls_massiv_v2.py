# Удаление из массива дублирующих элементов
import random
import numpy as np

from lesson_11.utils import generate_massiv


class Solution:
    massiv = generate_massiv()

    sorted_mass = np.sort(massiv).tolist()
    print(sorted_mass)
    
    i = 0
    while i <len(sorted_mass)-1:
        if sorted_mass[i] != sorted_mass[i+1]:
            i += 1
        else:
            del sorted_mass[i+1]
    print(sorted_mass)
