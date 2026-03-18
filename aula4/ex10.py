num = int(input('Digite um número inteiro: '))
numAux = num - 1
while numAux != 1:
    num *= numAux
    numAux -= 1
if num == 0:
    print(f'O fatorial do número é 1')
print(f'O fatorial do número é {num}')