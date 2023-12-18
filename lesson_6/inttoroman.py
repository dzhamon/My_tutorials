class Solution:
    def intToRoman(self, num: int) -> str:
        obshee_slovo=""
        num_str=str(num)
        while num_str != "":
            length = len(num_str)
            num = int(num_str[0])
            if length > 3:
				# 1000 -- +8
                slovo = num * "M"
            elif length == 3:
				# 100 -- 999
                if num == 0:
                    slovo = ""
                elif num > 0 and num < 4:
                    slovo = num * "C"
                elif num == 4:
                    slovo = "CD"
                elif num == 9:
                    slovo = "CM"
                else:
                    slovo = "D" + (num % 5) * "C"
            elif length == 2:
				# 10 -- 99
                if num == 0:
                    slovo = ""
                elif num > 0 and num < 4:
                    slovo = num * "X"
                elif num == 4:
                    slovo = "XL"
                elif num == 9:
                    slovo = "XC"
                else:
                    slovo = "L" + (num % 5) * "X"
            elif length == 1:
                if num < 4:
                    slovo = 'I' * num
                elif num == 4:
                    slovo = 'IV'
                elif num == 5:
                    slovo = 'V'
                elif num > 5 and num <9:
                    slovo = 'V' + 'I' * (num-5)
                elif num == 9:
                    slovo = 'IX'
            num_str = num_str[1:]
            obshee_slovo = obshee_slovo + slovo
        return obshee_slovo
