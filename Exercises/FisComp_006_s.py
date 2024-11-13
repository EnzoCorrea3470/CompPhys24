
s = "1.23,2.4,3.123"

a, b, c = (float(i) for i in s.split(","))
soma = a+b+c
print(soma)

# ou

Soma = sum(float(i) for i in s.split(","))
print(Soma)

