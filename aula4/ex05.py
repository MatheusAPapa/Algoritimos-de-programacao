x = float(input('Digite um número: '))
n = int(input('Digite o expoente: '))
numAux = x
while n != 1:
    numAux *= x
    n -= 1
print(numAux)