idade = int(input('Digite sua idade: '))
if idade > 18:
    peso = int(input('Digite seu peso'))
    if peso < 80:
        print('Peso médio')
    else: 
        print('Peso pesado')
else:
    print('Categoria juvenil')