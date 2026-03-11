x = int(input('Digite as cordenadas do ponto no eixo x: '))
y = int(input('Digite as cordenadas do ponto no eixo y: '))
if x > 0:
    if y > 0:
        print('O ponto está no 1º quadrante')
    else:
        print('O ponto está no 4º quadrante')
else:
    if y > 0:
        print('O ponto está no 2º quadrante')
    else:
        print('O ponto está no 3º quadrante')