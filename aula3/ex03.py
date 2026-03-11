a = int(input('Digite um número inteiro: '))
b = int(input('Digite outro número inteiro: '))
c = 0
if a == b:
    c = a + b
    print('O valor de c = a + b = {c}')
else:
    c = a * b
    print(f'O valor de c = a * b = {c}')