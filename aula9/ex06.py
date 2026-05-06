a = int(input('Digite um número: '))
b = int(input('Digite outro número: '))
qntEle = int(input('Digite a quantidade de números que terá na lista: '))
lista = []
intervalo = []
for i in range(qntEle):
    num = int(input('Digite um número: '))
    lista.append(num)   
for i in lista:
    if a > b:
        if a < num < b:
            intervalo.append(num)
    else:
        if b < num < a:
            intervalo.append(num)
print(f'Os números que está no intervalo [{a}; {b}] são: {intervalo}')