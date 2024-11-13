
a = float(input('Número: '))
x = 2
b = 0
while x <= 6:
    root = a ** (1/x)
    if root % 1 == 0:
        if root ** x == a:
            print('Seu par de inteiros é raíz {0} e potência {1}.'.format(root, x))
        x += 1
        b += 1
    else:
        x += 1
    if x == 7 and b == 0:
        print('Não há par de inteiros que satisfaz a condição.')