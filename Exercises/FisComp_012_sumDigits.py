"""
@author: Bruno O e Enzo C.

Finger exercise pag. 102 Do Livro 'Introduction to computation and programing using Python' John V. Guttag,
segunda ediçao.
"""

def sum_digits( s ):
    """Assumes s is a string
    Returns the sum of the decimal digits in s
    For example, if s is 'a2b3c' it returns 5"""
    summation = 0
    try:
        for c in s:
            if c.isdigit():
                summation += int(c)
        print('Sum:', summation)

    except TypeError:
        print('TypeError!')


sum_digits("H3LL0 P13tr0 1")


sum_digits(3.14)
