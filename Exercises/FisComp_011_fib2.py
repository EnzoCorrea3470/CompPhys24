# -*- coding: utf-8 -*-
"""
Created on Mon Nov  4 15:37:52 2024

@author: Bruno O e Enzo C.

Finger exercise pag. 54 Do Livro 'Introduction to computation and programing using Python' John V. Guttag, segunda edição.
"""

"""Finger exercise: When the implementation of fib in Figure 4.7 is used to compute
fib(5), how many times does it compute the value of fib(2) on the way to computing
fib(5)?"""

t = []

n = int(input('Int: '))
def fib(n):
    """Assumes n int >= 0
    Returns Fibonacci of n"""
    if n == 0 or n == 1:
        return 1
    if n == 2:
       t.append(1)
       return fib(n-1) + fib(n-2)
    else:
        return fib(n-1) + fib(n-2)

def testFib(n):
    for i in range(n+1):
        print('fib of', i, '=', fib(i))
        

testFib(n)
print('fib(2) foi chamado', sum(t), 'vezes')