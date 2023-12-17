# Сайт LeetCode. Задача 17 Letter Combination of a Phone Number
# В введенном телефонном номере (не более 4-х цифр, составить
# список комбинаций букв, написанных на клавишах цифр этого номера
class PhnNumLetComb:
	numlett_dict = {
		1: '00',2 : 'abc', 3 : 'def',
		4 : 'ghi', 5 : 'jkl', 6 : 'mno',
		7 : 'pqrs',	8 : 'tuv', 9 : 'wxyz'
	}
	lettersList = []
	def combination(self, Number):
		lst_digits = list(str(Number))
		for i in range(len(str(Number))-1):
			text = []
			combin = list([lst_digits[i]+lst_digits[i+1]])
			print(f"Комбинация букв для {combin}")
			a_tmp = []
			b_tmp = []
			a_tmp = list(self.numlett_dict.get(int(lst_digits[i])))
			b_tmp = list(self.numlett_dict.get(int(lst_digits[i+1])))
			for j in a_tmp:
				for k in b_tmp:
					if j != k:
						text.append(str(j+k))
			print(text)
			
app = PhnNumLetComb()
Number = int(input('Введите номер телефона - '))
print(f"Список комбинаций букв номера - {Number}")
lettersList = app.combination(Number)
