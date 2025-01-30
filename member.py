class member :
    def __init__(self, name, membership_id, borrowed_books):
        self.name = name
        self.membership_id = membership_id
        self.borrowed_books = []

    def borrowed_book(self, book):
        if book.get_available():
            book.set_available(False)

            self.borrowed_books.append(book)
            print(f'the book borrowed successfully', {book.get_title()})
        else:
            print(f'The book is not available now', {book.get_title()})
    def return_book(self, book):
        if book in self.borrowed_books:
            book.set_available(True)
            self.borrowed_books.remove(book)
            print(f'Book successfully returned', {book.get_title()})
        else:
            print(f'you did not borrowed the book', {book.get_title()})
    def get_name(self):
        return self.name
    def get_membership_id(self):
        return self.membership_id



member1 = member('Ibrahim', 112, ('The End of the World', 'Life and Death'))
member2 = member('Kareem', 1113, 'Good and Evil')