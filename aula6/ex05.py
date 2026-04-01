n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
n3 = int(input('Digite outro número: '))
def fatorial (n):
    if n < 0:
        print('Não existe fatorial de número negativo!')
    else:
        resultado = 1
        for i in range(1, n + 1):
            resultado *= i
        return resultado
print(f'O fatorial de {n1} é {fatorial(n1)}')
print(f'O fatorial de {n2} é {fatorial(n2)}')
print(f'O fatorial de {n3} é {fatorial(n3)}')