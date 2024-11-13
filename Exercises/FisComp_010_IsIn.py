"""
Created on Sat Nov 09 18:46:25 2024

@author: Bruno O e Enzo C.

Finger exercise pag. 42 Do Livro 'Introduction to computation and programing using Python' John V. Guttag, segunda edição.
"""

def isin(a, b):
    if a in b or b in a:
        return '{0} is in {1} (TRUE)'.format(a, b)
    else:
        return '{0} is not in {1} (FALSE)'.format(a, b)


a, b = input('A e B: ').split()
print(isin(a, b))
