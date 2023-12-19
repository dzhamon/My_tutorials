# Создать класс Person c аттрибутами name, age и методом introduce,
# который выводит информацию о человеке (например, "Меня зовут [name] и мне [age] лет").

class Person:
	def __init__(self, name, age, job):
		self.name = name
		self.age = age
		self.job = job
		
	def introduce(self):
		self.full_info = f"{self.name}, {self.age} years old. Hi is {self.job}"
		return self.full_info
	
	def happy_birthday(self):
		self.new_age = self.age + 1
		return self.new_age
	
class Student(Person):
	def __init__(self, name, age, job, student_id):
		super().__init__(name, age, job)
		self.student_id = student_id
		
	def student_info(self):
		return f"Student name is {self.name} His ID is {self.student_id}"
	
class Teacher(Person):
	def __init__(self, name, age, job, subject):
		super().__init__(name, age, job)
		self.subject = subject
		
	def teach(self):
		return f"{self.name} - teach {self.subject}"
		
		
if __name__ == '__main__':
	sarvar = Person('Sarvar', 25, 'engineer')
	turob = Person('Turobjon', 45, 'finance analist')
	anvar = Person('Anvar', 45, 'finance')
	artyom = Student('Artyom Vartazarov', 20, 'specialist', "ITgroup 1957")
	bekmurod = Teacher('Bek', 47, 'teacher', 'metall construtions' )
	olga = Teacher('Olga Mikhaylovna', 38, 'teacher','disign')
	


print(f"{artyom.name} is {artyom.job} and his student-id is {artyom.student_id}")

print('-------------------------------')

objects = (sarvar, turob, anvar, artyom, bekmurod, olga)
for obj in objects:
	obj.introduce()
	print(obj.full_info)
print('=============================')
for obj in objects:
	obj.happy_birthday()
	print('Now ', obj.name, 'age is ', '-->', obj.new_age, 'years old')
