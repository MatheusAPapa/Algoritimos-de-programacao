idade = int(input('Digite sua idade: '))
peso = float(input('Digite seu peso: '))
altura = int(input('Digite sua altura: '))
contHab = 0
media = 0
somaPeso = 0
qntPeso100 = 0
qntFilhos30_40 = 0
pessCFilho30_40 = 0
while idade > 0:
    contHab += 1
    somaPeso += peso
    media = somaPeso / contHab
    if 30 < idade < 40:
        pessCFilho30_40 += 1
        filhos30_40 = int(input('Quantos filhos você tem? '))
        qntFilhos30_40 += filhos30_40
        mediaFilhos30_40 = qntFilhos30_40 / pessCFilho30_40
    if peso > 100:
        qntPeso100 += 1
        percentualPeso = qntPeso100 / contHab
    idade = int(input('Digite sua idade: '))
    peso = float(input('Digite seu peso: '))
    altura = int(input('Digite sua altura: '))

print(f'''
{media}
{mediaFilhos30_40}
{percentualPeso}
''')