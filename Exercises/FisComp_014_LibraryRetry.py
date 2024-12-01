# -*- coding: utf-8 -*-
"""
Created on Sat Nov 30 20:42:21 2024

@author: Enzo C. e Bruno O.
"""

class Library(object):
    """ We want to construct a Library system, where we can add, remove, borrow 
        and return books."""
        
    def __init__(self):
        """ We want to have a way to track which books are added/removed from
            the system, as well as to track wheter they are available or have 
            been borrowed. For that, we use a dictionary to input books and
            have a boolean variable to that purpose. """
        
        self.books = {} #Library is empty as default
        
    def getBooks(self):
        """ Method for listing the books currently on the library. """
        
        list = []
        for book, available in self.books.items():
            if available == True:
                list.append(book)
        # The line above runs through the self.books dictionary and its
        # boolean, adding the corresponding book to the list if it is available
        if list:
            print("The available books in the library are:")
            for book in self.books:
                print(f"   - {book};")
        else:
            print("There are currently no books in the library!")
            
    def addBook(self, book_name):
        """ Method for adding books to the library. """
    
        self.books[book_name] = True    # By default, the book is avbailable
        # The ditionary only allows us to add an item together with it's value!!
        print(f"The book '{book_name}' has been added to the library!")
        
    def removeBbook(self, book_name):
        """ Method for removing books from the library. """
        
        self.books.pop(book_name)   # Removing the book from the dictionary
        print(f"The book '{book_name}' has been removed from the library!")
        
    def borrowBook(self, book_name):
        """ Method for borrowing a book from the library, changing it's status. """
        
        if self.books[book_name] == False: 
            print(f"The book {book_name} has already been borrowed!")
        else:
            self.books[book_name] = False    # Changing the book's status to unavailable
            print(f"The book {book_name} has been borrowed!")
        
    def returnBook(self, book_name):
        """ Method for returning a borrowed book to the library. """
        
        if self.books[book_name] == True:
            print(f"The book {book_name} was already on the library!")
        else:
            self.books[book_name] = True    # Changing the book's status to available
            print(f"The book {book_name} has been returned to the library!")
            

class User(object):
    """ We want to implement a user class to interact with the library."""
    
    def __init__(self, username):
        """ Here, we need a variable for the user's name and another for the 
            books they have currently borrrowed from the library. """
        
        self.username = username    # Variable for the user's name
        self.borrowed = []          # List for the books they have borrowed
        # Above does not need to be a dictionary for we need only the names
        
    def userGet(self):
        """ Method for the user to list it's borrowed books. """
    
        if len(self.borrowed) > 0:
            print(f"{self.username}'s borrowed book's are:")
            for book in self.borrowed:
                print(f"   - {book}")
        else:
            print(f"{self.username} has no booke currently borrowed from the library!")
    
    def userBorrow(self, lib, book_name):
        """ Method for the user to borrow books. """
        
        if lib.books.get(book_name) == True: # .get() returns the status of (book_name)
            lib.borrowBook(book_name)
            self.borrowed.append(book_name)
            print(f"{self.username} has borrowed the book {book_name}!")
        else:
            print(f"{self.username}, the book {book_name} is not available!")
        
    def userReturn(self, lib, book_name):
        """ Method for returning a borrowed book. """
        
        if lib.books.get(book_name) == False: # .get() returns the status of (book_name)
            lib.returnBook(book_name)
            self.borrowed.pop(book_name)
            print(f"{self.username}, the book {book_name} has been returned!")
        else:
            print(f"{self.username} the book {book_name} is already at the library!")


lib = Library()
lib.getBooks()
lib.addBook("The wise man's fear")
lib.addBook("The name of the wind")
lib.getBooks()

u = User("Bob")
print(u.username)
u.userBorrow(lib, "The wise man's fear")
u.userBorrow(lib, "The name of the wind")
print(lib.books.get("The name of the wind"))
print(lib.books.get("The wise man's fear"))
u.userGet()        