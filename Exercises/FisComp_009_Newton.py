
# -*- coding: utf-8 -*-
"""
Created on Mon Nov  4 15:37:52 2024

@author: Bruno O e Enzo C.

Finger exercise pag. 24 Do Livro 'Introduction to computation and programing using Python' John V. Guttag, segunda edição.
"""

# Find x such that x**2 - 25 is within epsilon of 0.01

epsilon = 0.01
k = 25.0
guess = k/2.0
numGuesses = 0
print('By Newton-Rephson method:')
while abs(guess*guess - k) >= epsilon:
 guess = guess - (((guess**2) - k)/(2*guess))
 numGuesses += 1
 print('The {}° approximation is'.format(numGuesses), guess)
print('The numGuesses by Newton-Rephson is', numGuesses)
print('Square root of', k, 'is about', guess)

print('\nBy bisection search method:')
numGuesses = 0
low = 0.0
high = max(1.0, k)
ans = (high + low)/2.0
while abs(ans**2 - k) >= epsilon:
 numGuesses += 1
 print('The {}° approximation is'.format(numGuesses), ans)
 if ans**2 < k:
   low = ans
 else:
   high = ans
 ans = (high + low)/2.0
print('The numGuesses by bisection search is', numGuesses)
print('Square root of', k, 'is about', ans)


