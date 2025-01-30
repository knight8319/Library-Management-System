class Book :
    def __init__(self, title, author, isbn, available=True): 
        self.title = title
        self.author = author
        self.isbn = isbn
        self.available = available

    def display_info(self) :
        available = 'availabe' if self.available else 'not available'
        print(f'title:{self.title}')
        print(f'author:{self.author}')
        print(f'isbn:{self.isbn}')
        print(f'availability:{available}')

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

member1 = 'member'(123, 'member1')
member2 = 'staffmember'(566, 'member2')

library.add_member(member1)
library.add_memer(member2)

member1.borrow_book(bool)

member1.return_book(bool)
