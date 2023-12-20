class Shape:
    def __init__(self, sides_number, name="Figura", *args):
        self.name = name
        self.sides_number = sides_number
        self.perimeter = None
        self.area = None
        self.sides = args


# triangle = Shape(name="Triangle", sides_number=3)
# rect = Shape(name="Rectangle", sides_number=4)
# print(triangle.sides_number)


class Circle(Shape):
    def __init__(self, radius):
        super().__init__(3, "Круг", radius)
        self._pi = 3.14
        self._radius = radius

    def area(self) -> int:
        return self._pi * self._radius * self._radius

    def get_area(self) -> str:
        return "Площадь круга: " + str(self.area())

    def perimeter(self) -> int:
        return 2 * self._pi * self._radius

    def get_perimeter(self) -> str:
        return "Длина окружности: " + str(self.perimeter())

# circle = Circle(7)
# print(circle.name)
# print(circle.sides_number)
# print(circle.sides)
