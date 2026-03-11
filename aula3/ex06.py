preco = float(input('Digite o preço do produto: '))
if preco > 100:
    preco *= 0.9
    print(f'desconto aplicado: {preco}')
else:
    print('não foi aplicado nenhum desconto')