# Представленное целое число конвертировать в римское представление
# Метод 2

class IntToRoman:
	Value = ['1', '4', '5', '6', '9', '10', '40', '50', '60', '70', '80', '90', '100', '500', '1000']
	Simbol = ['I', 'IV', 'V', 'VI', 'IX', 'X', 'XL', 'L', 'LX', 'LXX', 'LXXX', 'XC', 'C', 'D', 'M']
	my_dict = dict(zip(Value, Simbol))
	
	print(f"{my_dict}")
	n_rom = []
	
	def singleNum(self, a):
		n_rom = self.n_rom
		if a < 5 and a != 4:
			n_rom = 'I' * a
		if a == 4:
			n_rom = 'IV'
		if a == 5:
			n_rom = 'V'
		if a > 5 and a <9:
			n_rom = 'V' + 'I' * (a-5)
		if a == 9:
			n_rom = 'IX'
		return str(n_rom)
	def convert(self, N):
		text = ''
		if N == 0:
			print('Этот случай рассмотрим позже!')
			return
		while N > 0:
			print(N)
			for k in range(len(self.Value)-1, 0, -1):
				k_rom = int(self.Value[k])
				if N >= k_rom and k_rom != 10:
					res_tmp = N // k_rom
					if self.Value[k] in self.Value:
						text += self.my_dict[str(k_rom)] * res_tmp
					N = N % k_rom
				else:
					if k_rom < 10:
						text += self.singleNum(N)
						N = N // k_rom
					
		return text
			
	
app = IntToRoman()

Num = int(input('Введите целое число: '))

rom_view = app.convert(Num)
print(f"Римское представление Вашего числа - {rom_view}")