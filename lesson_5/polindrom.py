class Solution:
    def isPalindrome(self, x: int) -> bool:
	    new_x = str(x)[::-1]
	    if new_x == str(x):
		    return True
	    return False
    
num = int(input('Введите число, не менее двух цифр:'))
print("Ваше число полиндром ->", Solution().isPalindrome(num))