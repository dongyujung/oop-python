
# Abstraction and Encapsulation

# Implement a library management system which will handle the following tasks:
# Customer should be able to display all the books available in the library.
# Handle the process when a customer requests to borrow a book.
# Update the library collection when the customer returns a book.

# Class: library
# Layers of abstraction: display available books, lend a book, add a book.

# Class: customer
# Layers of abstraction: request for a book, return a book


class Library:
    
    def __init__(self, listOfBooks):
        self.availableBooks = listOfBooks
    
    def displayAvailableBooks(self):
        print()
        print("Available Books: ")
        for book in self.availableBooks:
            print(book)
    
    def lendBook(self, requestedBook):
        if requestedBook in self.availableBooks:
            print("You have now borrowed the book")
            self.availableBooks.remove(requestedBook)
        else:
            print("Sorry, the book is not available in our list.")
    
    def addBook(self, returnedBook):
        self.availableBooks.append(returnedBook)
        print("You have returned the book. Thank you.")
    
    
class Customer:
    def requestBook(self):
        print("Enter the name of a book you would like to borrow: ")
        self.book = input()
        return self.book
    
    def returnBook(self):
        print("Enter the name of the book which you are returning: ")
        self.book = input()
        return self.book


library = Library(['Think and Grow Rich', 'Who Will Cry When You Die', 'For One More Day'])
customer = Customer()

while True:
    print()
    print("Enter 1 to display the available books")
    print("Enter 2 to request for a book")
    print("Enter 3 to return a book")
    print("Enter 4 to exit")
    userChoice = int(input())
    
    if userChoice == 1:
        library.displayAvailableBooks()
    elif userChoice == 2:
        requestedBook = customer.requestBook()
        library.lendBook(requestedBook)
    elif userChoice == 3:
        returnBook = customer.returnBook()
        library.addBook(returnBook)
    elif userChoice== 4:
        quit()

