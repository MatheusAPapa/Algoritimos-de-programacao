nome = str(input('Digite seu nome: '))
sexo = str(input('Digite seu sexo [M/F]: '))
idade = int(input('Digite sua idade: '))
if sexo.upper() == 'F' and idade < 25:
    print('Aceita')
else: 
    print('Não aceita')