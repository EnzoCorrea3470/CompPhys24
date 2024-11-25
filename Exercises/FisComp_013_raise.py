# -*- coding: utf-8 -*-
"""
Created on Sun Nov  24 20:40:12 2024

@author: Bruno O. e Enzo C.

Finger exercise pag. 105 Do Livro 'Introduction to computation and programing using Python' John V. Guttag, segunda edição.
"""




def findAnEven(L):
    """Assumes L is a list of integers
    Returns the first even number in L
    Raises ValueError if L does not contain an even number"""

    for i in range(len(L)):
        if L[i] % 2 == 0:   
            return L[i]
    raise ValueError("Não há par na lista!")


L_1 = [1, 2, 3, 4]

print('O primeiro número par da lista 1 é:', findAnEven(L_1) )

L_2 = [1, 3, 5, 7]

try:
    print('O primeiro número par da lista 2 é:', findAnEven(L_2) )
except ValueError as errorMsg:
    print(errorMsg)
    