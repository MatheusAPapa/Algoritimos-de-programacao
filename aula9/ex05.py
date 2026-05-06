alunos = [[13, 1.53], [12, 1.39], [14, 1.60]]
cont = 0
for i in alunos:
    totalAlt += alunos[i][1]
media = totalAlt / len(alunos)
for i in alunos:
    if alunos[i][0] > 13:
        if alunos[i][1] > media:
            cont += 1
print(f'Dentre os 30 alunos {cont} possuem mais de 13 anos e altura maior que a média entre eles[{media}m]')