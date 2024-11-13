# Usando repetição

x = 0
t = 0
while x < 10:
    a = int(input('Digite um número inteiro: '))
    x += 1
    if a % 2 != 0 and a > t:
        t = a
if t == 0:
    print('Não há número impar')
else:
    print('O maior número impar é: ', t)