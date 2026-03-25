numeros = int(input('Quantos números terá na sequência? '))
a = 2
d = 3
aux = 0
soma = 0
for i in range(numeros):
    soma += a
    print(a)

    aux = a + d
    a = d
    d = aux
print(f'A soma dos números é {soma}')