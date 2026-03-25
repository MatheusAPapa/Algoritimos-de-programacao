num = float(input('Digite um número: '))
pares = 0   
impares = 0
mediaPar = 0
totalPar = 0
totalG = 0
cont = 0
while num != 0:
    if num % 2 == 0:
        pares += 1
        totalPar += 0
    else:
        impares += 1
    totalG += num
    cont += 1
    num = float(input('Digite um número: '))
print(f'''
A quantidade de números pares é {pares}
A quantidade de números impares é {impares}
A média dos números pares é {totalPar / pares}
A média dos números é {totalG / cont}
''')