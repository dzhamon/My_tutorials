class Book:
    name = "Harry Potter"
    year = 1998
    author = "Lawrens"
    invenarization_id = None

    def inventarization(self):
        self.invenarization_id = self.name.replace(" ", "") + ":" + str(self.year)


class Reader:
    fullname = "Artur"
    birth_date = 2004
    card_id = None
    books = []

    def register_to_library(self):
        self.card_id = str(self.fullname) + ":" + str(self.birth_date)


class Library:
    readers = []
    books = []

    # "Artur:1994"
    # "HarryPotter:1998"

    def __init__(self, org_name="Nur"):
        self.org_name = org_name

    def register_book(self, book: Book):
        book.inventarization()
        self.books.append(book)

    def register_reader(self, reader: Reader):
        reader.register_to_library()
        self.readers.append(reader)

    def otdavat_book_k_reader(self, book: Book, reader: Reader):
        ...

    def prinyat_book_ot_reader(self, book: Book, reader: Reader):
        ...

# nur_library = Library("Nur")
# sherlok_holms = Book()
# nur_library.register_book(sherlok_holms)
# nur_library.register_book(sherlok_holms)
# nur_library.register_book(sherlok_holms)
# nur_library.register_book(sherlok_holms)
# nur_library.register_book(sherlok_holms)
# nur_library.register_book(sherlok_holms)
