#Изучаем классы и все, что с ними связано

class Dog():
	def __init__(self, name, age): # конструктор, который построит модель собаки (имя и возраст)
		self.name = name
		self.age = age

	def sit(self): # метод, описывающий поведение собаки
		print(self.name, ' is now sitting')

	def roll_over(self): # метод, опимывающий поведение собаки
		print(self.name, ' rolled over!')

my_dog = Dog('Bobik', 6) # это экземпляр класса
your_dog = Dog('Sharik', 4)  # это тоже экземпляр класса

print('Мою собаку зовут ', my_dog.name)
print("Моему ", my_dog.name, ' ', my_dog.age, ' лет')

print('Твою собаку зовут ', your_dog.name)
print("Твоему ", your_dog.name, ' ', your_dog.age, ' лет')
your_dog.sit()
my_dog.roll_over()



class User:
	def __init__(self, first_name, last_name, adress):
		self.first_name = first_name
		self.last_name = last_name
		self.adress = adress

	def describe_user(self):
		print(f"{self.first_name} is engineer")
		print(f"{self.last_name} it his last name")
		print(f"{self.adress} - he(she) lives here ")

	def greet_user(self):
		print(f"{self.first_name} We are greeting you!")

our_boss = User('Анвар', 'Халилов', 'Dendropark')

print(f"{our_boss.first_name}")
our_boss.describe_user()
# ---------------------------------

our_collegue =User('Turob', 'Muzaffarov', 'Karasu')
our_collegue.describe_user()


