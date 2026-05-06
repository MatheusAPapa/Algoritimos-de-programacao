num = 0
par = []
impar = []
while num >= 0:
    num = int(input('Digite um número: '))
    if num % 2 == 0:
        par.append(num)
    else:
        impar.append(num)

print(f'''
Os números pares digitados foram: {par}
Os números impar digitados foram: {impar}
''')