palavra = str(input('Digite algo: '))
contrario = palavra[::-1]
if palavra == contrario:
    print(f'{palavra} é um palíndromo')
else:
    print(f'{palavra} não é um palindrmo')