num = int(input('Digite um número de 3 dígitos(ente 100 e 999): '))
#invertido = num[::-1]
#print(f'O número invertido fica assim: {invertido}')
#print(f'O número invertido é {num[2]}{num[1]}{num[0]}')
centena = num // 100
dezena = (num // 10) % 10
unidade = num % 10
invertido = unidade * 100 + dezena * 10 + centena
print(f'O número invertido é: {invertido}')