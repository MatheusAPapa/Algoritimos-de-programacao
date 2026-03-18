a = float(input('Digite um número: '))
b = float(input('Digite outro número: '))
c = float(input('Digite outro número: '))
maior = 0
if a == b == c:
    print('Todos são iguais')
elif a > b:
    if a > c:
        maior = a
    else:
        maior = c
elif b > c:
    maior = b
else:
    maior = c
print(f'O maior número é {maior}')