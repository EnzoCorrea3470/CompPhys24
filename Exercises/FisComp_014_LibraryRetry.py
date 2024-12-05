# -*- coding: utf-8 -*-
"""
Created on Sat Nov 30 20:42:21 2024

@author: Enzo C. e Bruno O.
"""

import Libs.Library as Library
import Libs.User as User


lib = Library.Library()
lib.getBooks()
lib.addBook("The wise man's fear")
lib.addBook("The name of the wind")
lib.getBooks()

u = User.User("Bob")
print(u.username)
u.userBorrow(lib, "The wise man's fear")
u.userBorrow(lib, "The name of the wind")
print("Is 'The wise man´s fear' available?",lib.books.get("The name of the wind"))
print("Is 'The name of the wind' available?", lib.books.get("The wise man's fear"))
u.userGet()        