#qnt números
n = int(input('Digite a quantidade de números à ser digitado: '))
#número
x = float(input('Digite um número: '))
n -= 1
maior = x
menor = x
if n >= 10:
    while n != 0:
        x = float(input('Digite outro número: '))
        if x > maior:
            maior = x
        elif x < menor:
            menor = x
        n -= 1
print(f'''
menor: {menor}
maior: {maior}
''')