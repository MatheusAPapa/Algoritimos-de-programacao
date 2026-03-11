a = int(input('Digite o valor de a da equação: '))
b = int(input('Digite o valor de b da equação: '))
c = int(input('Digite o valor de c da equação: '))
delta = b ** 2 - 4 * a * c
raiz1 = (-b + delta ** (1/2)) / 2 * a
raiz2 = (-b - delta ** (1/2)) / 2 * a
print(f'Os valores das raizes são {raiz1} {raiz2}')