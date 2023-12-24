import math


class Shape:
	def __init__(self, sides_number, name="Figura", *args):
		self.name = name
		self.sides_number = sides_number
		self.perimeter = None
		self.area = None
		self.sides = args


class Triangle(Shape):
	def __init__(self, a, b, c):
		self.sides_number = 3
		super().__init__(3, "Треугольник", 3)
		self.a = a
		self.b = b
		self.c = c
		self.perimetr = self.a + self.b + self.c
		self.semiperimetr = self.perimetr / 2
		self.area = math.sqrt(
			self.semiperimetr * (self.semiperimetr - self.a) *
			(self.semiperimetr - self.b) *
			(self.semiperimetr - self.c)
		)
	
	def get_area(self) -> str:
		return f"Площадь треугольника {self.area}"
	
	def get_perimetr(self) -> str:
		return f"Периметр треугольника {self.perimetr}"


# triangle = Shape(name="Triangle", sides_number=3)
# rect = Shape(name="Rectangle", sides_number=4)
# print(triangle.sides_number)
# print(triangle.name)

class Circle(Shape):
	def __init__(self, radius):
		super().__init__(3, "Круг", radius)
		self._pi = 3.14
		self._radius = radius
		self.area_data = self._pi * self._radius * self._radius
		self.circ_perimeter = 2 * self._pi * self._radius
		print(self.circ_perimeter)
	
	def get_semi_area(self):
		return "Половина площади круга равна: " + str(self.area_data / 2)
	
	def get_area(self) -> str:
		return f"Площадь круга: {self.area_data:.2f}"
	
	def get_perimeter(self) -> str:
		return f"Длина окружности - {self.circ_perimeter:.2f}"


triangle = Triangle(3, 4, 5)
print(triangle.get_perimetr())
print(triangle.get_area())

circle = Circle(7)
print(circle.get_perimeter())
print(circle.get_area())

#
#
# circle = Circle(7)
# print(circle.name)
# print(circle.sides_number)
# print(circle.sides)
#
#
# class Circle2(Shape):
#     def __init__(self, radius):
#         super().__init__(3, "Круг", radius)
#         self._pi = 3.14
#         self._radius = radius
#         self.area = self._pi * self._radius * self._radius
#         self.perimeter = 2 * self._pi * self._radius
#
#     def get_semi_area(self):
#         return "Половина площади круга равна: " + str(self.area / 2)
#
#     def get_area(self) -> str:
#         return "Площадь круга: " + str(self.area)
#
#     def get_perimeter(self) -> str:
#         return "Длина окружности: " + str(self.perimeter)

# circle = Circle2(7)
# print(circle.name)
# print(circle.sides_number)
# print(circle.sides)
