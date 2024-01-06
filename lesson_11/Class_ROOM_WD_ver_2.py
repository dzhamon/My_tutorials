# Лаборатория линуксоида. Композиция в ООП
class Room:
	room_sizes = {}
	def __init__(self, x, y, z):
		self.tup_room = (x, y, z)
		self.room_numb = 1
		self.square = 2 * z * (x + y)
		self.wd = []
	
	def add_wd(self, w, h):
		self.wd.append(WinDoor(w, h))
	
	def work_surface(self):
		new_square = self.square
		for i in self.wd:
			new_square -= i.square
		Room.room_sizes[self.room_numb] = self.tup_room
		self.room_numb += 1
		oboy_count = new_square / float(self.oboy_square)
		print(Room.room_sizes)
		return f"Для площади {new_square} вам понадобится {oboy_count} рулонов обоев"
		
	def oboy(self, x, y):
		self.oboy_square = WinDoor(x, y).square
		return self.oboy_square
class WinDoor:
	def __init__(self, x, y):
		self.square = x * y
	

r1 = Room(6, 6, 4)
r1.add_wd(1, 1)
r1.add_wd(1, 2)
r1.add_wd(1, 0.5)
r1.oboy(0.5, 5)
print(r1.work_surface())
r2 = Room(7, 8, 4.2)
r2.add_wd(1.5, 2)
r2.add_wd(1.5, 2)
r2.add_wd(1, 2)
r2.oboy(0.5, 5)
print(r2.work_surface())