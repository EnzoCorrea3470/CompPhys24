
# Se no programa original x < 0 o looping é infinito. Para corrigir isso:

x = -25
epsilon = 0.01
step = epsilon**2
numGuesses = 0
ans = 0.0
while abs(ans**2 - abs(x)) >= epsilon and ans <= abs(x):
 ans += step
 numGuesses += 1
print('numGuesses =', numGuesses)
if abs(ans**2 - abs(x)) >= epsilon:
 print('Failed on square root of', x)
else:
  if x >= 0:
    print(ans, 'is close to square root of', x)
  if x < 0:
    print('The imaginary number {}i is close to square root of'.format(ans), x)

# Agora o valor se aproxima inferiormente