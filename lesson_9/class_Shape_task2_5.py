# Создайте базовый класс Shape с методами area и perimeter.
# Создайте подклассы Circle, Rectangle и Triangle, реализующие методы
# area и perimeter для каждой геометрической фигуры.

class Shape:
	def __init__(self, size1, size2):
		self.size1 = size1
		self.size2 = size2
	
	def area_comm(self):
		self.area_tot = self.size1 * self.size2
		return self.area_tot


class Circle(Shape):
	def __init__(self, size1, size2):
		super().__init__(size1, size2)
		self.Pi = 3.14
	
	def circle_area(self):
		self.ar_circ = self.Pi * self.size1 ** 2
		return f"Площадь круга равна {self.ar_circ}"


class Triangle(Shape):
	def __init__(self, size3, size4):
		super().__init__(self.size1, self.size2)
		self.size3 = size3
		self.size4 = size4
	
	def triangle(self):
		self.rect_area = (self.size1 * self.size2) / 2
		""" это простой случай, когда один из size является высотой треугольника"""
		return f"Площадь треугольника равна {self.rect_area}"
	
	def perimetr(self):
		self.perim = self.size1 + self.size3 + self.size4
		""" можно было бы использовать формулу Герона для площади"""
		return (f"Периметр треугольника равен {self.perim}")


class Rectangle(Shape):
	def rect_area(self):
		self.area = self.size1 * self.size2
		return f"Площадь прямоугольника {self.area}"
	
	def perimetr(self):
		self.perim = (self.size1 + self.size2) * 2
		return f"Периметр прямоугольника равен {self.perim}"
