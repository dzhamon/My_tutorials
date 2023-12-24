# Создать класс Person c аттрибутами name, age и методом introduce,
# который выводит информацию о человеке (например, "Меня зовут [name] и мне [age] лет").

class Person:
	def __init__(self, *args, **kwargs):
		self.name = kwargs.get('name', None)
		self.age = kwargs.get('age', None)
		self.job = kwargs.get('job', None)
		self.hobbies = args
		
	def introduce(self):
		self.full_info = f"{self.name}, {self.age} years old. Hi is {self.job}"
		return self.full_info
	def happy_birthday(self):
		self.new_age = self.age + 1
		return f"В этом году ему исполнилось {self.new_age} года"
	
class Student(Person):
	def __init__(self, student_id, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.student_id = student_id

	def student_info(self):
		return f"Student name is {self.name} His ID is {self.student_id}"
	
class Teacher(Person):
	def __init__(self, subject, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.subject = subject

	def teach(self):
		return f"{self.name} - teaches {self.subject}"



sarvar = Person('reading', 'programming', 'avtomobile', job='programmer', name= 'sarvar', age=23)
archik = Student('FPM_77', 'engineer', name='Artyom', age=20, job='student')
bek = Teacher('chemistry', name='Bekmurod', age=45, job='teacher')
print(archik.introduce())
print(archik.student_info())
print(bek.introduce())
print(bek.teach())
print(sarvar.introduce())
print(sarvar.happy_birthday())












