class Car:
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
		print(f"Пробег машины составляет {self.odometer_reading} километровю")
		
	def update_odometer(self, mileage): # это изменение значения атрибута в коде
		self.odometer_reading = mileage
		
class ElectricCar(Car):
	def __init__(self, make, model, year, battery_size):
		super().__init__(make, model, year)
		self.battery_size = battery_size
	def charge_battery(self):
		return f"Размер батареи авто {self.battery_size} ампер"
	
	def check_battery_status(self, discharge):
		self.chrg_batt -= discharge
	
	
my_car = Car('Chevrolet','Lacetty', '2009')
my_old_car = Car('Moskvich', '412', 1972)
my_collegue_car = ElectricCar('BWD', 'Cherry', '2023', 9000)

print(my_collegue_car.get_descriptive_name())

my_car.odometer_reading = 365000 # это прямое изменение значения атрибута
my_car.read_odometer()
my_car.update_odometer(8000) # в метод update_odometer передается значение пробега (mileage)
my_car.read_odometer()

print(my_old_car.get_descriptive_name())


