class Car():
	def __init__(self, make, model, year):
		self.make = make
		self.model = model
		self.year = year
		self.odometer_reading = 0 #атрибут не объявлен в self. Поэтому присвоено значение 0
		
	def get_descriptive_name(self):
		"""возвращает аккуратно отформатированное описание"""
		long_name = f"{self.make} {self.model} {self.year} "
		return long_name.title()
	
	def read_odometer(self):
		"""выводит пробег"""
		print(f"This car has {self.odometer_reading} miles on it.")
		
	def update_odometer(self, mileage): # это изменение значения атрибута в коде
		self.odometer_reading = mileage
	
my_new_car = Car('audi','A4', '2019')
print(my_new_car.get_descriptive_name())
my_new_car.read_odometer()
my_new_car.odometer_reading = 23 # это прямое изменение значения атрибута
my_new_car.read_odometer()
my_new_car.update_odometer(23000) # в метод update_odometer передается значение пробега
my_new_car.read_odometer()

my_old_car = Car('Moskvich', '412', 1972)
print(my_old_car.get_descriptive_name())
print(my_old_car.read_odometer())
