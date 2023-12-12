# источник - книга Марк Лютц Изучаем Python
"""
Декораторы в Python — это функции, которые принимают другую функцию
в качестве аргумента, добавляют к ней некоторую дополнительную функциональность
и возвращают функцию с измененным поведением.
"""
"""
class Spam:
	numInstances = 0
	def __init__(self):
		Spam.numInstances = Spam.numInstances + 1
	@staticmethod
	def printNumInstances():
		print('Number of instances created: ', Spam.numInstances)
		
a = Spam()
b = Spam()
c = Spam()
Spam.printNumInstances()
a.printNumInstances()
print("====================================")
# ---------------------------------------
"""



class tracer:
	def __init__(self, func):
		self.calls = 0
		self.func = func
	def __call__(self, *args):
		self.calls += 1
		print('call %s to %s' % (self.calls, self.func.__name__))
		self.func(*args)
@tracer
def spam(a, b, c):
	print(a, b, c)

spam(1, 2, 3)
spam('a', 'b', 'c')
spam(4, 5, 6)



# Вариаент кода без декоратора

# calls = 0
# def tracer(func, *args):
# 	global calls
# 	calls += 1
# 	print('call %s to %s' % (calls, func.__name__))
# 	func(*args)
# def spam(a, b, c):
# 	print(a, b, c)
#
# spam(1,2,3)