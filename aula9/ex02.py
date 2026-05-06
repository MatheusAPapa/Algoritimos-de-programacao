qntEle = int(input('Digite a quantidade de números que terá na lista[no máximo 20]: '))
lista = []
cont = 0
if qntEle > 20:
    qntEle = int(input('Digite a quantidade de números que terá na lista[no máximo 20]: '))
for i in range(qntEle):
    num = int(input('Digite um número: '))
    lista.append(num)

for i in lista:
    if i % 3 == 0:
        cont += 1

print(f'A quantidade de números divisíveis por 3 é {cont}')