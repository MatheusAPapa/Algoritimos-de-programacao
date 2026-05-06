qntEle = int(input('Digite a quantidade de números que terá na lista[no máximo 10]: '))
lista = []
maior = 0
menor = 100000
if qntEle > 10:
    qntEle = int(input('Digite a quantidade de números que terá na lista[no máximo 10]: '))
for i in range(qntEle):
    num = int(input('Digite um número: '))
    lista.append(num)
for i in lista:
    if num < menor:
        menor = num
    elif num > maior:
        maior = num

print(f'Maior: {maior} \nMenor: {menor}')