idade = 10
nomeVelha = ''
velha = 0
nomeJovem = ''
jovem = 100
while idade > 0:
    nome = str(input('Digite seu nome: '))
    idade = int(input('Digite sua idade: '))
    if idade > 0:
        if idade > velha:
            velha = idade
            nomeVelha = nome
        elif idade < jovem:
            jovem = idade
            nomeJovem = nome

print(f''' 
A pessoa mais velha é a/o {nomeVelha} com {velha} anos
A pessoa mais nova é a/o {nomeJovem} com {jovem} anos
''')