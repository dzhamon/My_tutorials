# Удаление дубликатов из отсортированного массива
import random
import numpy as np
class Solution:
	massiv = []
	n = 0
	while n != 15:
		massiv.append(random.randint(2,20))
		n += 1
	sorted_mass = np.sort(massiv)
	print(sorted_mass)
	
	def dim_reduction(self, my_array, k):
		i = 0
		while i < k:
			if my_array[i] < my_array[i+1]:
				i += 1
			else:
				array_temp = my_array.pop[i+1]
				break
		return array_temp

	while True:
		dim_reduction(mass_copy, n)
		