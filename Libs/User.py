# -*- coding: utf-8 -*-
"""
Created on Sat Nov 30 20:42:21 2024

@author: Enzo C. e Bruno O.
"""

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
