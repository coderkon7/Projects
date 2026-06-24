class Book():
    def __init__(self, title, author, is_borrowed=False):
        self.title = title
        self.author = author
        self.is_borrowed = is_borrowed
    
    def borrow(self):
        if self.is_borrowed == False:
            self.is_borrowed = True
            print(f"Succesfully borrowed the book: {self.title} by {self.author}.")
        else:
            print(f"Failed to borrow book ({self.title} by {self.author}). Reason: Someone borrowed this book.")
        
    def return_book(self):
        if self.is_borrowed == True:
            self.is_borrowed = False
            print(f"Succesfully returned the book: {self.title} by {self.author}.")
        else:
            print(f"Failed to return book. Reason: This book ({self.title} by {self.author}) isn't borrowed!")

# Note that these books and/or authors may not be real
book1 = Book("Trivia Questions", "John")
book2 = Book("The World of Animals", "John")
book3 = Book("Garden City", "Alex")

for book in [book1,book2,book3]:
    book.borrow()
    book.return_book()

book1.borrow()
book1.borrow()