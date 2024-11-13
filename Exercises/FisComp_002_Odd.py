# -*- coding: utf-8 -*-
"""
Created on Mon Nov  4 15:37:52 2024

@author: Física - UEL
"""

x = 5
y = -1
z = 6
t = 0

if x % 2 == 0 and y % 2 == 0 and z % 2 == 0:
    print('Nenhum valor é ímpar.')
else:
    if x % 2 != 0:
        t = x
    if y % 2 != 0 and y > t:
        t = y
    if z % 2 != 0 and z > t:
        t = z
    print('O maior valor é: ', t)