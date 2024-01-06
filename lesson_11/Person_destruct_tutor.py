class Person:
	def __init__(self, first_name, last_name, qualification=1):
		self.first_name = first_name
		self.last_name = last_name
		self.qualification = qualification
	def pers_descript(self):
			return f"Имя {self.first_name}, фамилия {self.last_name}, квалификация {self.qualification}"

pers = [Person('Bob', 'Marley', 3),
        Person('Dody', 'Klark', 1),
        Person('Ricky', 'Smith', 4),
        Person('Dandy', 'Biden', 1),
        ]

kamol = Person('Kamol', 'Jamol', 'student')
print(kamol.pers_descript())

k = 0
for person in pers:
	print(person.pers_descript())
	if person.qualification == 1:
		print("До свидания, мистер ", person.last_name, " ваша должность сокращена.")
		pers.pop(k)
		k += 1





# По условию задачи нужно было использовать __del__ У меня не получилось.




