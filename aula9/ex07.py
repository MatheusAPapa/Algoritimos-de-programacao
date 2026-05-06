gab = ['a', 'b', 'e', 'c', 'e', 'd', 'a', 'e', 'c', 'c']
alunos = []
for i in range(10):
    nome = str(input('Digite o nome do aluno: '))
    nota = 0
    for i in range(10):
        questao = str(input(f'digite a resposta da questão {i+1}: '))
        if questao == gab[i]:
            nota += 1
    alunos.append([nome, nota])

for i in alunos:
    totalNota += alunos[i][1]
media = totalNota / len(alunos)
print(alunos)
print(f'A média da sala foi de {media} pontos')