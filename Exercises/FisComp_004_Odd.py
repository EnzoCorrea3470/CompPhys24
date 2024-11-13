
# Sem usar estrutura de repetição

a, b, c, d, e, f, g, h, i, j = (int(i) for i in input("Digite 10 números inteiros: ").split())
t = 0

if a % 2 != 0:
    t = a
if b % 2 != 0 and b > t:
    t = b
if c % 2 != 0 and c > t:
    t = c
if d % 2 != 0 and d > t:
    t = d
if e % 2 != 0 and e > t:
    t = e
if f % 2 != 0 and f > t:
    t = f
if g % 2 != 0 and g > t:
    t = g
if h % 2 != 0 and h > t:
    t = h
if i % 2 != 0 and i > t:
    t = i
if j % 2 != 0 and j > t:
    t = j
if t == 0:
    print('Não há número impar')
else:
    print('O maior número impar é: ', t)

    

