class Table:
	def __init__(self, l=1, w=1, h=1):
		self.length = l
		self.width = w
		self.height = h
		if isinstance(self, KitchenTable):
			p = int(input('Сколько мест: '))
			self.places = p
class DeskTable(Table):
	def square(self):
		return self.width * self.length
class ComputerTable(DeskTable):
	def square(self, monitor=0.0):
		return self.length * self.width - monitor # можно ли здесь использовать square от DeskTable??
class KitchenTable(Table):
	def __init__(self, l=1, w=1, h=0.7, p=4):
		Table.__init__(self, l, w, h)
		self.places = p
	def set_places(self, p):
		self.places = p
		print(t4.square())
		
t4 = KitchenTable(2, 3, 0.7)
t4.places =6
print(t4.set_places(6))
	
t1 = Table(1.5, 1.8, 0.75)
t2 = DeskTable(2.0, 1.5, 0.8)
print(t2.square())
t3 = ComputerTable(0.8, 0.6, 0.7)
print(t3.square(0.3))