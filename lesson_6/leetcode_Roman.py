# Источник - leetcode.com
#Задача 3. Конвертирование целого числа в римское представление

class IntToRoman:
    Simbol = [
        'I', 'V', 'X', 'L', 'C', 'D', 'M'
    ]
    Value = [
        '1', '5', '10', '50', '100', '500', '1000'
    ]
    my_dict = dict(zip(Value, Simbol))
    print(f"{my_dict}")
    n_rom = []
    def singlenum(self, a):
        # global n_rom
        n_rom = self.n_rom
        if a in [4, 9]:
            if a < 5:
                value = self.Value[0]
                print(value)
                n_rom = self.my_dict.get(str(value)) * int(a)
            elif a == 5:
                n_rom = 'V'
            elif a > 5 and a < 9:
                n_rom = 'V' + 'I' * (a - 5)
                print(a, ' --> ', n_rom)
            else:
                n_rom = 'IV' if a // 5 == 0 else 'IX'
        return n_rom
        
    def convert(self, N):
        text = ''
        if N <= 0:
            print('Решение будет рассмотрено позже')
            return
        else:
            # здесь должен быть код разложения двух-(и более) значного числа на составляющие цифры,
            # вызов для каждой функции app.singlenum(a) и, в зависимости от значности числа поиск
            # соответствующего римского представления (567 = 5*100 + 6 * 10 + 7 <==> DLXVII
            
            text += app.singlenum(N)
        return text
                
                
app = IntToRoman()

number = int(input('Введите целое число: '))
rom_view = app.convert(number)
print(f"Римское представление Вашего числа - {rom_view}")