num = int(input('Digite um número: '))
def numPerfeito(n):
    soma = 0
    cont = 1
    while cont < n:
        if n % cont == 0:
            soma += cont
        cont += 1
    if soma == n:
        print(f'número {n} é perfeito')
    else:
        print(f'número {n} não é perfeito')
numPerfeito(num)