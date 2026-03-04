vCompra = int(input('Digite o valor da compra: '))
vPagamento = int(input('Digite o valor dado pelo cliente: '))
troco = vPagamento - vCompra
print(f'\nCompra: {vCompra}')
print(f'Pagamento: {vPagamento}')
print(f'Troco: {troco}')
print('\nEM:')

notaCem = troco // 100
sobra = troco - notaCem * 100
print(f'100$ - {notaCem} cédulas')

notaCinquenta = sobra  // 50
sobra -= notaCinquenta * 50
print(f'50$ - {notaCinquenta} cédulas')

notaVinte = sobra // 20
sobra -= notaVinte* 20
print(f'20$ - {notaVinte} cédulas')

notaDez = sobra // 10
sobra -= notaDez * 10
print(f'10$ - {notaDez} cédulas')

notaCinco = sobra // 5
sobra -= notaCinco * 5
print(f'5$ - {notaCinco} cédulas')

print(f'1$ - {sobra} cédulas')