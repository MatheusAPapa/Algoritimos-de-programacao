comprimento = float(input('Qual o comprimento do terreno? '))
largura = float(input('Qual a largura do terreno? '))
precoM = float(input('Qual o preço do m? '))
resultado = (comprimento * 2) + (largura * 2) * precoM
print(f'O valor para construir nesse terreno é de {precoM} reais')