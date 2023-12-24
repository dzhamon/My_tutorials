class Library:
	book_name = ['12 стульев', 'Золотой теленок', 'Буранный полустанок',
	             'Спитамен', 'Война и мир', 'Капитанская дочка', 'Изучаем Python']
	autor = ['Ильф Петров', 'Ильф Петров', 'Айтматов',
	         'Камар Амон', 'Лев Толстой', 'Александр Пушкин', 'Марк Лутц']
	publish_year = ['1977', '1977', '1985', '2003', '1968', '1972', '2017']
	dict_books = dict(zip(book_name, zip(autor, publish_year)))
	
	book_readers = ['Сарвар', 'Даврон', 'Туроб', 'Анвар', 'Дилшод', 'Бекмурод']
	dict_readers = dict(zip(book_readers, book_name))
	
	def __init__(self, dict_books, dict_readers):
		self.dict_books = dict_books
		self.book_name = book_readers
	
	def add_book(self, book_title):
		if book_title not in self.dict_books.keys():
			self.dict_books[book_title] = Book(book_title)
	
	def issue_book(self, title):
		pass


class Book(Library):
	def __init__(self, title=''):
		super().__init__(self.dict_books, self.book_readers)
		self.title = title
	
	def add_book_found(self, title, author, publish_year):
		self.dict_books[title] = (author, publish_year)
		return f"{self.dict_books} - книга добавлена в хранилище"


print(

)
# anvar = Library()
# 	def get_book(self, reader):
# 		self.book_name = input('Введите название книги : - ')
# 		if self.book_name in dict_book
#
# 	def recieve(self, ):
#
# class Member:
# 	member_name =
