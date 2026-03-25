num = float(input('Digite um número: '))
cont = 0
maior = num
segMaior = 0
while cont < 10:
    if num > maior:
        maior = num
    elif num > segMaior:
        segMaior = num
    cont += 1
    num = float(input('Digite um número'))
print(f'Os maiores números são {maior} e {segMaior}''')
