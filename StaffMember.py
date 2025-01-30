from member import member
from Book import Book

class Staffmember(member):
    def __init__(self, staff_id):
        super().__init__(staff_id)
        self.staff_id = staff_id

    def add_book(self, book):
        print(f'A book has been added to the library')

    def get_staff_id(self):
        return self.staff_id
    

class library:
    def __init__(self):
        self.book = []
        self.members = []

    def add_book(self, book):
        self.__books.append(book)

    def get_books(self):
        return self.__books

    def get_members(self):
        return self.__members
    

library = library()

Book1 = Book('The End of the World', 'Mohamed', 9778760, True)
Book2 = Book('Good and Evil', 'Metwaly', 9778733, True)
Book3 = Book('Life and Death', 'Elsharawy', 97781372, True)

library.add_book(Book1)
library.add_book(Book2)

member1 = member('Ibrahim', 112, Book1)
member2 = Staffmember('Kareem', 1113, Book3)

library.add_member(member1)
library.add_memer(member2)


member1.borrow_book(bool)

member1.return_book(bool)

print(Book1, member)
