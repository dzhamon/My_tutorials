# источник - книга Эрик Мэтиз - Изучаем Python

class Car():
	"""Простая модель автомобиля."""
	def __init__(self, make, model, year):
		self.make = make
		self.model = model
		self.year = year
		self.odometer_reading = 0
	def get_descriptive_name(self):
		long_name = f"{self.make} {self.model} {self.year}"
		return long_name.title()
	def read_odometer(self):
		print(f"This car has {self.odometer_reading} miles on it.")
	def update_odometer(self, mileage):
		if mileage >= self.odometer_reading:
			self.odometer_reading = mileage
		else:
			print("You can't roll back an odometer!")
	def increment_odometer(self, miles):
		self.odometer_reading += miles
		
	def fill_gas_tank(self):
		print('The value of tank is 60 litres')
		
class ElectricalCar(Car): # это потомок класса Car
	def __init__(self, make, model, year):
		super().__init__(make, model, year) # специальная функция, которая позволит вызвать метод родителя
											# еще __init__ и super называют магическими функциями.
											# super вызывает метод __init_ родительского класса, и тогда
											# потомок получает доступ ко всем атрибутам родилеского класса
		self.battery_size = 75
		
	def describe_battery(self):
		""" выводит информацию о мощности аккумулятора"""
		print(f"This car has a {self.battery_size}-kwa in houre")
		
	""" так как для электромобиля заправка бензином бессмысленна, этот метод  в классе-потомке можно переопределить"""
	def fill_gas_tank(self):
		print("This car does not need gas tank")
		
	"""В случае, если класс-потомок увеличился в размерах, то часть его, к которой относятся методы
	касающиеся , например, батарем, можно вынести в отдельный class Battery(). Об этом см в книге, стр 184"""
		
my_tesla = ElectricalCar('tesla', 'model s', 2019) # несмотря на то, что в классе-потомке
														# несмотря на то, что классе-потомке есть единственный метод super,
print(my_tesla.get_descriptive_name())    # экземпляр с tesla прекрасно выводит атрибуты электроавтомобиля
my_tesla.describe_battery()
my_tesla.fill_gas_tank()

my_car = Car('Chevrolet', 'Traker 2', 2022)
my_car.get_descriptive_name()
print(my_car.get_descriptive_name())
my_car.fill_gas_tank()

