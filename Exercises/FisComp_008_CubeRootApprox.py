""""
low parameter should consider the minimum value between x and 0, as much as the parameters squared should be cubed.
"""
x = -64
epsilon = 0.01
numGuesses = 0
low = min(0.0, x)
high = max(1.0, x)
ans = (high + low)/2.0
while abs(ans**3 - x) >= epsilon:
    print('low =', low, 'high =', high, 'ans =', ans)
    numGuesses += 1
    if ans**3 < x:
        low = ans
    else:
        high = ans
    ans = (high + low)/2.0
print('numGuesses =', numGuesses)
print(ans, 'is close to square root of', x)
max