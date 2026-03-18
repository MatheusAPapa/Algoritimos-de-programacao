par = 0
impar = 0
parar = 'n'
while parar != 'n':
    n = float(input('Digite um número: '))
    if n % 2 == 0:
        par += n
    else:
        impar += 1
    parar = str(input('Deseja para de adicionar números [s/n]:')).lower
print(f'O resultado da soma dos pares é {par}')
print(f'Forma digitados {impar} números impares')