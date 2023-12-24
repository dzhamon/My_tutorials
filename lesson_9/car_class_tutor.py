class Car:
	def __init__(self, **kwargs):
		self.odometer_reading = kwargs.get('odometer_reading', None)
		self.make = kwargs.get('make', None)
		self.year = kwargs.get('year', None)
		self.model = kwargs.get('model', None)
	
	def get_descriptive_name(self):
		"""возвращает аккуратно отформатированное описание"""
		self.long_name = (f"Производитель {self.make}, модель {self.model}, "
		                  f" Год выпуска {self.year}")
		return self.long_name
	
	def read_odometer(self):
		"""выводит пробег"""
		print(f"Пробег машины составляет {self.odometer_reading} километров")
	
	def update_odometer(self, mileage):  # это изменение значения атрибута в коде
		self.odometer_reading += mileage
		
class ElectricCar(Car):
	def __init__(self, **kwargs):
		super().__init__(**kwargs)
		self.battery = Battery()
		
	
class Battery():
	def __init__(self, battery_size = 108.8):
		self.battery_size = battery_size
		
	def describe_battery(self):
		return f"Мощность батареи этого авто - {self.battery_size} кВт-ч"
	def get_range(self):
		""" приблизительный запас хода аккумулятора """
		if self.battery_size == 75:
			self.range = 270
		elif self.battery_size == 108.8:
			self.range = 350
		return f"This car can go about {self.range} miles on a full charge."
		
		
	

my_car = Car(make='Chevrolet', model='Lacetti', odometer_reading=330000, year=2009)
print(my_car.get_descriptive_name())
print(my_car.read_odometer())

anvar_car = Car(make='Uzavto', model='Nexia 3', odometer_reading=23000, year=2021)
print(anvar_car.get_descriptive_name())

your_car = ElectricCar(make='BYD', model='Tang EV', year=2022)
print(your_car.get_descriptive_name())
print(your_car.battery.describe_battery())

print(your_car.battery.get_range())

