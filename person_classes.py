# источник книга Mark Lutz Программирование на Python, том 1

class Person:
	def __init__(self, name, age, pay=0, job=None):
		self.name = name
		self.age = age
		self.pay = pay
		self.job = job
		
	def lastName(self):
		return self.name.split()[-1]
		
	def giveRaise(self, percent):
		self.pay *= (1.0 + percent)
		
	def get_descriptive_name(self):
		"""возвращает аккуратно отформатированное описание"""
		long_name = f"{self.name} {self.age} {self.pay} {self.job}"
		return long_name.title()
		
# class Manager(Person): # это потомок класса Person. Наследует все свойства родителя
# 	def __init__(self, name, age, pay):
# 		Person.__init__(name, age, pay, 'manager')
# 	def giveRaise(self, percent, bonus=0.1):
# 		Person.giveRaise(self, percent + bonus)

	
class Manager(Person): # а можно было здесь иметь свой конструктор (__int__) ???
	def givRaise(self, percent, bonus=0.1):
		self.pay *= (1.0 + percent + bonus)
	
if __name__ == '__main__':
	bob = Person('Bob Smith', 42, 30000, 'software')
	sue = Person('Sue Jones', 45, 40000, 'hardware')
	john = Person('John Biden', '82', 20000, 'congressmen')
	# здесь спросить про tom ???
	

	print(bob.name, sue.pay)
	sue.giveRaise(.10)
	print(sue.pay)
	print('--------------------')
	tom = Manager(name='Tom Doe', age=50, pay=50000) # экз класса Manager, потомок родителя Person
	print(tom.lastName()) # здесь он использует метод из родителя
	tom.giveRaise(.10) # здесь он использует метод родителя который изменяет pay
	print(tom.pay) # получаем новый pay для Tom
	# print(tom.job()) Написав это вывод мы получим ошибку, тк у класса Manager нет конструктора.
	# Чтобы избежать этого мы должны явным образом прописать в Manager конструктор его родителя
	print('---------------------')
	print(bob.get_descriptive_name())
	print(john.get_descriptive_name())
	print(tom.get_descriptive_name())
	print(sue.get_descriptive_name())
	print('Проверка работы полиморфизма :')
	db = [bob, tom, john, sue]
	
	for obj in db:
		obj.giveRaise(0.1)
		print(obj.lastName(), ' --> ', obj.pay)
		
		
	